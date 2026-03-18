#!/usr/bin/env python3
"""
Flask API for Emotional Support Website
Provides REST endpoints for the Next.js frontend with:
- Chat history persistence
- Sentiment analysis
- Crisis detection with regional hotlines
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from dotenv import load_dotenv
from datetime import datetime
import json
from textblob import TextBlob
import re

# Load environment variables
load_dotenv()

# Import AI assistants
try:
    from ai_assistant_openai import get_openai_response, get_openai_status
except ImportError:
    get_openai_response = None
    get_openai_status = None

try:
    from ai_assistant_claude import get_claude_response
except ImportError:
    get_claude_response = None

try:
    from ai_assistant_gemini import get_gemini_response
except ImportError:
    get_gemini_response = None

# Firebase (optional - can use file-based storage if Firebase not available)
try:
    import firebase_admin
    from firebase_admin import credentials, db, initialize_app
    FIREBASE_ENABLED = False
    try:
        # Try to initialize Firebase if service account key exists
        if os.path.exists('serviceAccountKey.json'):
            cred = credentials.Certificate('serviceAccountKey.json')
            firebase_admin.initialize_app(cred, {
                'databaseURL': os.getenv('FIREBASE_DB_URL', '')
            })
            FIREBASE_ENABLED = True
    except Exception as e:
        print(f"Firebase initialization failed: {e}")
except ImportError:
    FIREBASE_ENABLED = False

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Crisis keywords by severity
CRISIS_KEYWORDS = {
    'critical': [
        'kill myself', 'suicide', 'want to die', 'end my life',
        'kill myself', 'should die', 'rather be dead',
        'no reason to live', 'better off dead', 'how to overdose',
        '自殺', '自杀', 'tự tử'  # Chinese, Vietnamese
    ],
    'high': [
        'self harm', 'cut myself', 'hurt myself',
        'depression', 'hopeless', 'worthless', 'can\'t go on',
        '自傷', '自伤', 'tự gây hại'
    ],
    'moderate': [
        'sad', 'lonely', 'stressed', 'anxiety', 'panic',
        'overwhelmed', 'crying'
    ]
}

# Regional hotlines
HOTLINES = {
    'HK': {'number': '2389 2222', 'name': '撒瑪利亞防止自殺會 (Samaritans Hong Kong)', 'country': 'Hong Kong'},
    'TW': {'number': '1925', 'name': '安心專線 (Lifeline Taiwan)', 'country': 'Taiwan'},
    'CN': {'number': '010-8295 1332', 'name': '北京心理援助熱線', 'country': 'Mainland China'},
    'SG': {'number': '1800-221-4444', 'name': 'Samaritans Singapore', 'country': 'Singapore'},
    'MY': {'number': '03-4101-6100', 'name': 'Befrienders Malaysia', 'country': 'Malaysia'},
}

# In-memory chat storage (fallback if Firebase not available)
chat_storage = {}

# Helper functions
def analyze_sentiment(text):
    """Analyze sentiment of text using TextBlob"""
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity  # -1 (negative) to 1 (positive)
        subjectivity = blob.sentiment.subjectivity  # 0 (objective) to 1 (subjective)
        
        # Convert polarity to mood
        if polarity > 0.5:
            mood = 'positive'
        elif polarity < -0.5:
            mood = 'negative'
        else:
            mood = 'neutral'
        
        return {
            'mood': mood,
            'polarity': polarity,
            'subjectivity': subjectivity
        }
    except:
        return {'mood': 'neutral', 'polarity': 0, 'subjectivity': 0}

def detect_crisis(text):
    """Detect crisis indicators in text"""
    text_lower = text.lower()
    crisis_level = 'none'
    confidence = 0.0
    matched_keywords = []
    
    for level, keywords in CRISIS_KEYWORDS.items():
        for keyword in keywords:
            if keyword.lower() in text_lower:
                matched_keywords.append((keyword, level))
                if level == 'critical':
                    crisis_level = 'critical'
                    confidence = 1.0
                elif level == 'high' and crisis_level != 'critical':
                    crisis_level = 'high'
                    confidence = max(confidence, 0.8)
                elif level == 'moderate' and crisis_level == 'none':
                    crisis_level = 'moderate'
                    confidence = max(confidence, 0.5)
    
    return {
        'crisis_level': crisis_level,
        'confidence': confidence,
        'keywords': matched_keywords
    }

def save_chat_message(session_id, role, content, sentiment=None, crisis_info=None):
    """Save chat message to storage"""
    if session_id not in chat_storage:
        chat_storage[session_id] = []
    
    message = {
        'timestamp': datetime.now().isoformat(),
        'role': role,
        'content': content,
        'sentiment': sentiment,
        'crisis': crisis_info
    }
    chat_storage[session_id].append(message)
    return message

def get_chat_history(session_id):
    """Get chat history for a session"""
    return chat_storage.get(session_id, [])

# Routes
@app.route('/', methods=['GET'])
def serve_index():
    """Serve the HTML frontend"""
    try:
        return send_from_directory('.', 'index.html')
    except FileNotFoundError:
        # Fallback to API info if index.html not found
        return jsonify({
            'message': 'Emotional Support AI API',
            'version': '1.0',
            'endpoints': {
                'health': '/api/health',
                'chat': '/api/chat',
                'chat_history': '/api/chat-history/<session_id>',
                'analyze': '/api/analyze',
                'assistants': '/api/assistants',
                'hotlines': '/api/hotlines'
            }
        })

@app.route('/<path:filename>', methods=['GET'])
def serve_static(filename):
    """Serve static files"""
    try:
        return send_from_directory('.', filename)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

@app.route('/api/root', methods=['GET'])
def api_root():
    """API endpoints info"""
    return jsonify({
        'message': 'Emotional Support AI API',
        'version': '1.0',
        'endpoints': {
            'health': '/api/health',
            'chat': '/api/chat',
            'chat_history': '/api/chat-history/<session_id>',
            'analyze': '/api/analyze',
            'assistants': '/api/assistants',
            'hotlines': '/api/hotlines'
        }
    })

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    openai_runtime = {
        'package_available': False,
        'key_set': bool(os.getenv('TEAMPLUS_API_KEY') or os.getenv('OPENAI_API_KEY') or os.getenv('OPENROUTER_API_KEY')),
        'mode': 'unknown',
        'client_initialized': False,
        'ready': False,
        'init_error': 'openai status unavailable',
    }
    if get_openai_status:
        try:
            openai_runtime = get_openai_status()
        except Exception as e:
            openai_runtime['init_error'] = f'failed to read openai status: {e}'

    return jsonify({
        'status': 'ok',
        'environment': 'production',
        'message': 'Emotional Support API is running',
        'firebase': FIREBASE_ENABLED,
        'openai': {
            'handler_loaded': get_openai_response is not None,
            **openai_runtime
        }
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Chat endpoint for AI responses with sentiment analysis and crisis detection
    
    Request:
    {
        "message": "user message",
        "assistant_type": "openai" | "claude" | "gemini",
        "session_id": "optional session identifier"
    }
    
    Response:
    {
        "response": "AI response text",
        "assistant": "openai" | "claude" | "gemini",
        "sentiment": {"mood": "positive|negative|neutral", "polarity": -1 to 1},
        "crisis": {"crisis_level": "none|moderate|high|critical", "confidence": 0-1},
        "hotline": {...} (if crisis detected)
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400
        
        message = data.get('message')
        assistant_type = data.get('assistant_type', 'openai').lower()
        session_id = data.get('session_id', 'default')
        region = data.get('region', 'HK')
        options = data.get('options', {})
        
        # Analyze incoming message
        user_sentiment = analyze_sentiment(message)
        crisis_info = detect_crisis(message)
        
        # Save user message
        save_chat_message(session_id, 'user', message, user_sentiment, crisis_info)
        
        # Get AI response - use OpenAI if available
        response_text = None
        used_assistant = None
        
        if get_openai_response:
            response_text = get_openai_response(message, options=options)
            used_assistant = 'openai'
        else:
            return jsonify({'error': 'OpenAI API not configured. Please set OPENAI_API_KEY.'}), 500
        
        if not response_text:
            return jsonify({'error': 'No response from AI service'}), 500
        
        # Analyze AI response
        ai_sentiment = analyze_sentiment(response_text)
        
        # Save AI response
        save_chat_message(session_id, 'assistant', response_text, ai_sentiment)
        
        # Prepare hotline info if crisis detected
        hotline = None
        if crisis_info['crisis_level'] in ['critical', 'high']:
            hotline = HOTLINES.get(region, HOTLINES['HK'])  # Default to HK
        
        return jsonify({
            'response': response_text,
            'assistant': used_assistant,
            'sentiment': ai_sentiment,
            'crisis': crisis_info,
            'hotline': hotline,
            'success': True
        })
    
    except RuntimeError as e:
        # RuntimeError is used for OpenAI availability/API failures in assistant layer.
        print(f"Runtime error in /api/chat: {str(e)}")
        msg = str(e)
        if 'connection error' in msg.lower():
            return jsonify({'error': msg, 'success': False}), 503
        if 'OpenAI is not available' in msg:
            return jsonify({'error': msg, 'success': False}), 503
        if 'OpenAI API error' in msg:
            return jsonify({'error': msg, 'success': False}), 502
        return jsonify({'error': msg, 'success': False}), 500
    except Exception as e:
        print(f"Error in /api/chat: {str(e)}")
        return jsonify({'error': f'Server error: {str(e)}', 'success': False}), 500

@app.route('/api/chat-history/<session_id>', methods=['GET'])
def get_history(session_id):
    """Get chat history for a session"""
    try:
        history = get_chat_history(session_id)
        return jsonify({
            'session_id': session_id,
            'history': history,
            'count': len(history)
        })
    except Exception as e:
        print(f"Error in /api/chat-history: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """Analyze a message without AI response"""
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'Message is required'}), 400
        
        message = data.get('message')
        
        sentiment = analyze_sentiment(message)
        crisis = detect_crisis(message)
        
        return jsonify({
            'sentiment': sentiment,
            'crisis': crisis,
            'success': True
        })
    except Exception as e:
        print(f"Error in /api/analyze: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/assistants', methods=['GET'])
def assistants():
    """Get available assistants - only OpenAI for this deployment"""
    return jsonify({
        'assistants': [
            {
                'name': 'openai',
                'display': 'OpenAI GPT',
                'icon': '🤖'
            }
        ],
        'default': 'openai'
    })

@app.route('/api/hotlines', methods=['GET'])
def get_hotlines():
    """Get emergency hotlines"""
    return jsonify({
        'hotlines': HOTLINES
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV', 'development') == 'development'
    
    print("\n" + "="*60)
    print("🚀 Emotional Support API Server v2")
    print("="*60)
    print(f"Starting on http://localhost:{port}")
    print(f"Debug mode: {debug}")
    print(f"Firebase: {'Enabled' if FIREBASE_ENABLED else 'Disabled (using in-memory storage)'}")
    print("="*60 + "\n")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )

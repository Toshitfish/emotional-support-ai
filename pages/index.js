import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';

export default function Home() {
  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [assistantType, setAssistantType] = useState('claude');
  const [sessionId] = useState(() => 'session_' + Math.random().toString(36).substr(2, 9));
  const [isCrisis, setIsCrisis] = useState(false);
  const [hotline, setHotline] = useState(null);
  const [currentMood, setCurrentMood] = useState(null);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [chatHistory]);

  const getMoodColor = (mood) => {
    switch (mood) {
      case 'positive':
        return 'bg-green-100 text-green-800 border-green-300';
      case 'negative':
        return 'bg-red-100 text-red-800 border-red-300';
      case 'neutral':
        return 'bg-gray-100 text-gray-800 border-gray-300';
      default:
        return 'bg-gray-100 text-gray-800 border-gray-300';
    }
  };

  const getMoodEmoji = (mood) => {
    switch (mood) {
      case 'positive':
        return '😊';
      case 'negative':
        return '😔';
      case 'neutral':
        return '😐';
      default:
        return '🤔';
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!message.trim()) return;

    setLoading(true);
    const userMessage = message;
    setMessage('');

    try {
      // Add user message to history
      setChatHistory((prev) => [
        ...prev,
        { role: 'user', content: userMessage, sentiment: null, crisis: null },
      ]);

      // Send to API
      const response = await axios.post('/api/chat', {
        message: userMessage,
        assistantType,
        session_id: sessionId,
        region: 'HK', // Default region
      });

      const { response: aiResponse, sentiment, crisis, hotline: hotlineInfo } = response.data;

      // Add AI response to history
      setChatHistory((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: aiResponse,
          sentiment,
          crisis,
        },
      ]);

      setCurrentMood(sentiment?.mood || null);

      // Update crisis status
      if (crisis?.crisis_level === 'critical' || crisis?.crisis_level === 'high') {
        setIsCrisis(true);
        setHotline(hotlineInfo);
      } else {
        setIsCrisis(false);
        setHotline(null);
      }
    } catch (error) {
      console.error('Error:', error);
      setChatHistory((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: `Error: ${error.response?.data?.error || error.message}`,
          sentiment: null,
          crisis: null,
        },
      ]);
      setIsCrisis(false);
      setHotline(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-blue-100 p-4">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-lg shadow-lg p-6 mb-4">
          <div className="flex items-center justify-between mb-4">
            <div>
              <h1 className="text-4xl font-bold text-indigo-600 mb-2">
                💙 Emotional Support
              </h1>
              <p className="text-gray-600">
                AI-powered assistant that listens without judgment
              </p>
            </div>
            {currentMood && (
              <div className={`px-4 py-2 rounded-lg border-2 font-semibold text-lg ${getMoodColor(currentMood)}`}>
                {getMoodEmoji(currentMood)} {currentMood}
              </div>
            )}
          </div>
        </div>

        {/* Crisis Alert */}
        {isCrisis && hotline && (
          <div className="bg-red-50 border-2 border-red-400 rounded-lg p-4 mb-4 animate-pulse">
            <div className="flex items-start gap-3">
              <span className="text-3xl">🆘</span>
              <div className="flex-1">
                <h3 className="font-bold text-red-800 text-lg mb-2">Crisis Support Available</h3>
                <p className="text-red-700 mb-3">
                  Please reach out to someone you trust or contact a crisis helpline:
                </p>
                <div className="bg-white rounded p-3 border-l-4 border-red-500">
                  <p className="font-bold text-red-900">{hotline.name}</p>
                  <p className="text-2xl font-mono text-red-700 mt-1">{hotline.number}</p>
                  <p className="text-sm text-gray-600 mt-1">{hotline.country}</p>
                </div>
                <p className="text-red-700 mt-3 text-sm">
                  If you are in immediate danger, please call emergency services (911, 999, or local equivalent).
                </p>
              </div>
            </div>
          </div>
        )}

        {/* Chat Area */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
          {/* Chat History */}
          <div className="lg:col-span-2 bg-white rounded-lg shadow-lg p-4 flex flex-col" style={{ height: '500px' }}>
            <div className="overflow-y-auto flex-1 mb-4 space-y-4">
              {chatHistory.length === 0 ? (
                <div className="text-center text-gray-400 py-8">
                  <p className="text-lg">Start a conversation...</p>
                  <p className="text-sm mt-2">Share what's on your mind, and I'm here to listen.</p>
                </div>
              ) : (
                chatHistory.map((msg, idx) => (
                  <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                    <div
                      className={`max-w-xs px-4 py-2 rounded-lg ${
                        msg.role === 'user'
                          ? 'bg-indigo-600 text-white rounded-br-none'
                          : 'bg-gray-200 text-gray-800 rounded-bl-none'
                      }`}
                    >
                      <p className="text-sm">{msg.content}</p>
                      {msg.sentiment && msg.role === 'assistant' && (
                        <p className="text-xs mt-2 opacity-75">
                          Mood: {getMoodEmoji(msg.sentiment.mood)} {msg.sentiment.mood}
                        </p>
                      )}
                    </div>
                  </div>
                ))
              )}
              <div ref={messagesEndRef} />
            </div>

            {/* Input Form */}
            <form onSubmit={handleSubmit} className="border-t pt-4">
              <div className="mb-3">
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  AI Assistant
                </label>
                <select
                  value={assistantType}
                  onChange={(e) => setAssistantType(e.target.value)}
                  disabled={loading}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
                >
                  <option value="claude">Claude 🧠</option>
                  <option value="openai">OpenAI 🤖</option>
                  <option value="gemini">Gemini ✨</option>
                </select>
              </div>

              <div className="flex gap-2">
                <textarea
                  value={message}
                  onChange={(e) => setMessage(e.target.value)}
                  placeholder="Share what's on your mind..."
                  disabled={loading}
                  rows="3"
                  className="flex-1 px-3 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-indigo-500 focus:border-transparent resize-none"
                />
                <button
                  type="submit"
                  disabled={loading || !message.trim()}
                  className={`px-4 py-2 rounded-lg font-semibold text-white transition-colors ${
                    loading || !message.trim()
                      ? 'bg-gray-400 cursor-not-allowed'
                      : 'bg-indigo-600 hover:bg-indigo-700'
                  }`}
                >
                  {loading ? '...' : 'Send'}
                </button>
              </div>
            </form>
          </div>

          {/* Sidebar - Info & Resources */}
          <div className="bg-white rounded-lg shadow-lg p-6 space-y-4">
            <div>
              <h3 className="font-bold text-lg text-indigo-600 mb-3">💡 How It Works</h3>
              <ul className="space-y-2 text-sm text-gray-700">
                <li>✓ Express yourself freely</li>
                <li>✓ Judgment-free support</li>
                <li>✓ Anonymous & private</li>
                <li>✓24/7 availability</li>
              </ul>
            </div>

            <div className="border-t pt-4">
              <h3 className="font-bold text-lg text-gray-700 mb-3">⚠️ Important</h3>
              <p className="text-sm text-gray-600">
                This AI is not a replacement for professional mental health care. If you're in crisis, please contact a mental health professional or crisis hotline.
              </p>
            </div>

            <div className="border-t pt-4">
              <h3 className="font-bold text-gray-700 mb-2">Emergency Region</h3>
              <select
                disabled
                defaultValue="HK"
                className="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm bg-gray-50 text-gray-600"
              >
                <option>HK - Hong Kong</option>
                <option>TW - Taiwan</option>
                <option>CN - Mainland China</option>
                <option>SG - Singapore</option>
                <option>MY - Malaysia</option>
              </select>
              <p className="text-xs text-gray-500 mt-2">For later versions, you can change your region here.</p>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="mt-6 text-center text-sm text-gray-600">
          <p>Session ID: {sessionId}</p>
          <p className="mt-2">Made with ❤️ for emotional support</p>
        </div>
      </div>
    </div>
  );
}

import axios from 'axios';

const PYTHON_BACKEND_URL = process.env.PYTHON_BACKEND_URL || 'http://localhost:5000';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { message, assistantType, session_id, region } = req.body;

  if (!message) {
    return res.status(400).json({ error: 'Message is required' });
  }

  try {
    // Call Python backend
    const response = await axios.post(`${PYTHON_BACKEND_URL}/api/chat`, {
      message,
      assistant_type: assistantType || 'claude',
      session_id: session_id || 'default',
      region: region || 'HK',
    }, {
      timeout: 30000,
    });

    return res.status(200).json({
      response: response.data.response || response.data.message || 'No response',
      sentiment: response.data.sentiment || null,
      crisis: response.data.crisis || null,
      hotline: response.data.hotline || null,
    });
  } catch (error) {
    console.error('Backend error:', error.message);
    
    // Return error response
    if (error.response) {
      return res.status(error.response.status).json({
        error: error.response.data?.error || 'Backend error',
      });
    }
    
    return res.status(500).json({
      error: 'Failed to reach AI service. Make sure Python backend is running.',
    });
  }
}

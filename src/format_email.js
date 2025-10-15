const briefing = $input.first().json.briefing_text;

// Create the date string for the header
const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
const dateString = new Date().toLocaleDateString('en-US', options);
const simpleDate = new Date().toLocaleDateString();

const emailBody = `
<!DOCTYPE html>
<html>
<head>
<style>
  body { font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.6; color: #333; background: #f5f5f5; }
  .container { max-width: 600px; margin: 20px auto; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
  .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; text-align: center; color: white; }
  .content { padding: 30px; }
  .footer { background: #f8f9fa; padding: 20px; text-align: center; font-size: 12px; color: #666; }
  h1 { margin-top: 0; }
  .briefing-content { white-space: pre-wrap; text-align: left; } /* Preserves AI line breaks */
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>🌅 Abu Dhabi Morning Brief</h1>
    <p>${dateString}</p>
  </div>
  <div class="content">
    <div class="briefing-content">${briefing}</div>
  </div>
  <div class="footer">
    <p>Automated by your n8n + Gemini AI system</p>
    <p>Day 2 of 180 - AI Engineer Journey 🚀</p>
  </div>
</div>
</body>
</html>
`;

return [
  {
    json: {
      subject: `🌅 Abu Dhabi Morning Brief - ${simpleDate}`,
      body: emailBody
    }
  }
];

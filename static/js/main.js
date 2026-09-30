document.addEventListener('DOMContentLoaded', () => {
  const messageField = document.getElementById('message');
  const platformField = document.getElementById('platform');
  const button = document.getElementById('scan');
  const result = document.getElementById('result');

  button.addEventListener('click', async () => {
    const text = messageField.value.trim();
    const platform = platformField.value;

    if (!text) {
      result.textContent = 'Please enter a message first.';
      return;
    }

    const response = await fetch('/api/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, platform })
    });

    const data = await response.json();
    if (data.status === 'success') {
      result.innerHTML = `
        <strong>Score:</strong> ${data.analysis.score}<br>
        <strong>Level:</strong> ${data.analysis.level}<br>
        <strong>Source:</strong> ${data.analysis.source}<br>
        <strong>Recommendations:</strong>
        <ul>${data.analysis.recommendations.map(r => `<li>${r}</li>`).join('')}</ul>
      `;
    } else {
      result.textContent = data.message || 'An error occurred.';
    }
  });
});

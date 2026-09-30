from app import app


def test_index_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'AI Scam Message Detector' in response.data


def test_analyze_route():
    client = app.test_client()
    response = client.post('/api/analyze', json={
        'text': 'URGENT: Your bank account is blocked. Verify your PIN immediately.',
        'platform': 'sms'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert data['analysis']['score'] >= 60

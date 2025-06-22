import pytest
from unittest.mock import patch
from app.services import summarization

@patch("app.services.summarization.requests.post")
def test_summarize_text_mock(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "response": "La Tierra gira alrededor del Sol provocando las estaciones."
    }

    input_text = "La Tierra gira alrededor del Sol en una órbita elíptica..."
    result = summarization.summarize_text(input_text)

    assert isinstance(result, str)
    assert "Tierra" in result or "Sol" in result
    print("Resumen simulado:", result)

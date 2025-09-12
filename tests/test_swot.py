from src.swot import generate_swot_chat

def test_generate_swot_chat():
    description = "Mobile app to help people find local farmers' markets."
    result = generate_swot_chat(description)
    assert isinstance(result, dict)
    assert "strengths" in result or "raw_output" in result

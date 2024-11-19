from app.utils import check_endpoint

def test_check_endpoint():
    endpoint = {"name": "TestAPI", "url": "https://api.github.com"}
    result = check_endpoint(endpoint)
    assert result["status"] == 200
    assert result["response_time"] > 0

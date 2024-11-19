import requests

def check_endpoint(endpoint):
    try:
        response = requests.get(endpoint['url'], timeout=5)
        return {
            "name": endpoint["name"],
            "status": response.status_code,
            "response_time": response.elapsed.total_seconds()
        }
    except requests.exceptions.RequestException as e:
        return {
            "name": endpoint["name"],
            "status": "Error",
            "response_time": None,
            "error": str(e)
        }

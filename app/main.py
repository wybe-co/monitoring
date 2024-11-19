import json
from flask import Flask, jsonify
from utils import check_endpoint
from database import SessionLocal, APILog

app = Flask(__name__)

@app.route("/monitor", methods=["GET"])
def monitor_apis():
    with open("app/endpoints.json") as f:
        endpoints = json.load(f)

    logs = []
    session = SessionLocal()
    for endpoint in endpoints:
        result = check_endpoint(endpoint)
        logs.append(result)
        # Salva no banco
        log = APILog(
            name=result["name"],
            status=result["status"],
            response_time=result["response_time"]
        )
        session.add(log)
    session.commit()
    session.close()

    return jsonify(logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
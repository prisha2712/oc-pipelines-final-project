from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify({"application": "oc-pipelines-final-project", "status": "running"})


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

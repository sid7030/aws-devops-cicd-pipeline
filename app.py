from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello DevOps! AWS CI/CD Pipeline is working."


@app.route("/about")
def about():
    return jsonify({
        "project": "AWS DevOps CI/CD Pipeline",
        "technology": "Flask",
        "container": "Docker",
        "automation": "Jenkins",
        "deployment": "AWS EC2"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
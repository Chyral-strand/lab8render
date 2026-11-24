import flask
import requests
app = flask.Flask(__name__)
@app.route("/", methods=["GET"])
def hello():
    url = "https://service1-381052179472.europe-west2.run.app"
    response = requests.get(url)
    return(response.content)

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
from flask import Flask, make_response
app = Flask(__name__)

@app.route("/")
def index():
    return "fdk"

@app.route("/no_content")
def no_content():
    return ({"message":"No content found"}, 204)

@app.route("/exp")
def index_explicit():
    resp = make_response({"message":"exp side"})
    resp.status_code = 200
    return resp
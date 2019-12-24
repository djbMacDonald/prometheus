from flask import Flask, request, render_template, jsonify, Response
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/listen", methods=['POST'])
def listen():
  data = request.get_json(force=True)
  return data

if __name__ == "__main__":
  app.run()

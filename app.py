from flask import Flask
import connexion

# app = Flask(__name__)

# Connecting swagger ui with Flask app
app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/", methods=['GET', 'POST'])
def welcome() -> str: 
    return "Hello World"

if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=3000, debug=True)
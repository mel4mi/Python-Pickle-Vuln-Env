import pickle
import base64
from flask import Flask, request, render_template



app = Flask(__name__)



@app.route("/",methods=["GET"])
def main():
        if request.method == "GET":
            return render_template("index.html")           


@app.route("/pickle_d", methods=["POST"])
def pickle_d():
    data = base64.urlsafe_b64decode(request.form['pickled'])
    deserialized = pickle.loads(data)
    return render_template('pickled.html',  unpickled_data=deserialized)


if __name__ == "__main__":
    app.run()
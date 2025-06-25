from crypt import methods

from flask import Flask,request,render_template,jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler



application = Flask(__name__)
app = application

model = pickle.load(open("flask/models/ridge.pkl", "rb"))
scaler = pickle.load(open("flask/models/scaler.pkl", "rb"))




@app.route("/")
def home():
    return render_template("hello.html")

@app.route("/predict",methods = ["GET","POST"])
def predict():
    if request.method == "POST":
        Temprature = float(request.form.get("Temprature"))
        Rh = float(request.form.get("RH"))
        ws = float(request.form.get("Ws"))
        rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))
        Classes = float(request.form.get("Classes"))
        Region = float(request.form.get("Region"))


        X_scaled = scaler.transform([[Temprature,Rh,ws,rain,FFMC,DMC,ISI,Classes,Region]])
        predict = model.predict(X_scaled)

        return render_template("pred.html",result = predict[0])
    else:
        return render_template("pred.html")




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
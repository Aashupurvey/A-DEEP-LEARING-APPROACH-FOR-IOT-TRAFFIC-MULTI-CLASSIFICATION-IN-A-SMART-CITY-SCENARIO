from flask import Flask, request, jsonify, render_template,flash
import pickle
import sklearn
import pandas as pd
from markupsafe import Markup
app = Flask(__name__)
model = pickle.load(open('models/randomf.pkl', 'rb'))

dataset = pd.read_csv("cleandata.csv")
def IotDeviceName(inbytes,protocol,ip,ipv4,mac):
    for index, row in dataset.iterrows():
        if row['IPunique']==ip and row['IPV4_SRC_ADDRunique']==ipv4 and row['MACunique']==mac:
            ipen= row['IPencoded']
            ipv4en = row['IPV4_SRC_ADDRencoded']
            macen = row['MACencoded']
            ypred = model.predict([[inbytes,protocol,ipen,ipv4en,macen]])
            if ypred[0]==1:
                print("Non_IOT")
                return "Non_IOT","Non_IOT"
            else:
                print("IOT")
                device = row['devicecmodelunique']
                return "IOT",device
        else:
            return "device_not_found","device_not_found"
    
   
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    try: 
        inbytes = request.form['inbytes']
        protocol =  request.form['protocol']
        ip = request.form['ip']
        ipv4 = request.form['ipv4']
        mac = request.form['mac']
        ttype, device = IotDeviceName(inbytes,protocol,ip,ipv4,mac)
        return render_template('index.html', ttype = ttype, device= device )
    except:
        message = Markup("<h3>Failed! Invalid data</h3>")
        flash(message)
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

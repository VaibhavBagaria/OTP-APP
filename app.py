# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define route and Verify_otp() function below
@app.route('/login', methods=['POST'])
def verify_otp():
    username=request.form['username']
    password=request.form['password']
    number=request.form['number']
    if username=='verify' and password == '12345':
        Account_SID='AC7cb268e176920e3c31b48a23914d547a'
        Auth='770bc3d78bc6e6f48dfcbe8400b5947d'
        Service_SID='VA1dd0128d3626aca4861b4bc849b165a9'
        client=Client(Account_SID, Auth)
        verification = client.verify \
            .services(Service_SID) \
            .verifications \
            .create(to=number, channel='sms')
        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return "Entered User ID or Password is wrong"

if __name__ == "__main__":
    app.run(debug=True)


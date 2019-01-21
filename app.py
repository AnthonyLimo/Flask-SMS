from flask import Flask, request, render_template

import os

import africastalking


app = Flask(__name__)

username = "sandbox"
api_key = "f6c6e1d0686fddddb375d47c8bcda0dc80713f214ce26b912567ab156ae7feee"
africastalking.initialize(username,api_key)

@app.route("/", methods=["GET","POST"])
def main():
    if request.method == "POST":
        sms_message = request.form["smsMessage"]
        phone_number = request.form["phoneNumber"]

        print(sms_message)
        print(phone_number)

        response = sms.send(sms_message,[phone_number])
        print(response)

        

    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=os.environ.get('PORT'),debug=True)

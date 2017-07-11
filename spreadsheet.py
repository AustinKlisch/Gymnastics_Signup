import gspread
from oauth2client.service_account import ServiceAccountCredentials

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)
def test():
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    sheet = client.open("Gymnastics Sign Up").sheet1
    from_number = request.values.get('Body', None)
    sheet.update_cell(1, 1, from_number)

if __name__ == "__main__":
    app.run(debug=True)
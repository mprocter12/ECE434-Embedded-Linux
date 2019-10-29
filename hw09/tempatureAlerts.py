#!/usr/bin/env python3

# Mark Procter
# ECE434
# Homework 9

# while True:


#     pass

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import smbus
import time

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1ggW83WNoR0cbjVklPcgcfQbznsnnmuyi9GPFUNQnAJw'
RANGE_NAME = 'A2'

# temp sensor setup
bus = smbus.SMBus(2)
tempSensors = [0x48, 0x49]

def main():
     """Shows basic usage of the Sheets API.
    Writes values to a sample spreadsheet.
    """
    store = file.Storage('tokenPython.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    tempC0 = bus.read_byte_data(tempSensors[0], 0)
    tempF0 = tempC0*(9/5)+32

    # Call the Sheets API
    # Compute a timestamp and pass the first two arguments
    values = [ [time.time()/60/60/24+ 25569 - 4/24, sys.argv[1], sys.argv[2]]]
    body = { 'values': values }
    result = service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID,
                            range=RANGE_NAME,
                            #  How the input data should be interpreted.
                            valueInputOption='USER_ENTERED',
                            # How the input data should be inserted.
                            # insertDataOption='INSERT_ROWS'
                            body=body
                            ).execute()
    
    updates = result.get('updates', [])
    # print(updates)

    if not updates:
        print('Not updated')


if __name__ == '__main__':
    main()

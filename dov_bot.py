from __future__ import print_function

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters
import logging
import sqlite3


from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



def start():
        CREDENTIALS_FILE = 'creds.json'
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

        spreadsheet_id = "1WMDgMbqIuy4tutcw4ZxC27Pr1_IvgexPNNrNWOS5Y6k"

        values = service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {"range": "A2:A3",
                    "majorDimension": "COLUMNS",
                    "values": [["Питання 1", "Питання 2"]]}
                    ]
            }
        ).execute()

start()

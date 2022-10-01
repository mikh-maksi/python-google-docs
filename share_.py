from __future__ import print_function

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


# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = '/Users/mac/Documents/work/python/python-google-docs/creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '163ZHfU1HS8vqWnW0HTUlQNKZc1FR9Y1rloIq48oRWt4'

# 1ZVIdm4fUrf-1mJIPVw1nem9f6fGcXScLZ9xZ8ZH86Ck
# 1QHdENZb91-V_xRqil3DATRlKshHvhYfKQVds4LweoNw

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)


# title = 'ASPIRIn - Docs'

# spreadsheet = {
#     'properties': {
#         'title': title
#     }
# }
# spreadsheet = service.spreadsheets().create(body=spreadsheet,
#                                             fields='spreadsheetId').execute()
        
# new_sheet_id = format(spreadsheet.get('spreadsheetId'))
# print(new_sheet_id)


1c37Koz0H0sonZ8vBNTxWdIoTZpJyqP2syU6ykFa3Px8
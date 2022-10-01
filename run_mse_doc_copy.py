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

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v3', http = httpAuth)


# title = 'ASPIRIn - Docs'

# spreadsheet = {
#     'properties': {
#         'title': title
#     }
# }
# spreadsheet = service.spreadsheets().create(body=spreadsheet,
#                                             fields='spreadsheetId').execute()
# print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))



file_id = '1aGDasJE9-QpVVBONYlG7vO_ko9eMzxsCVL57LSsJksg'
folder_id = '1VWbyfFhi_3ueZLE43irYgwkmWfLJcLgY'
# Retrieve the existing parents to remove
file = drive_service.files().get(fileId=file_id,
                                 fields='parents').execute()
previous_parents = ",".join(file.get('parents'))
# Move the file to the new folder
file = drive_service.files().update(fileId=file_id,
                                    addParents=folder_id,
                                    removeParents=previous_parents,
                                    fields='id, parents').execute()


# source_file_id = "163ZHfU1HS8vqWnW0HTUlQNKZc1FR9Y1rloIq48oRWt4"
# folder_ids = ['1VWbyfFhi_3ueZLE43irYgwkmWfLJcLgY','12eYnOYWmVe4KdIA72UcGQVG9O7-DzCfv']

# file_metadata = {
#     'name' : 'ASPIRIn - document',
#     'parents':folder_ids,
#     'starred': True,
#     'description':'Document for analysis of business'
# }
# service.files().copy(
#     fileId=source_file_id,
#     body = file_metadata
# ).execute()




# for i in range(45):
#     print(i)
#     k = i+1
#     values = service.spreadsheets().values().get(
#     spreadsheetId=spreadsheet_id,
#     range=f"A{k}:R{k}",
#     majorDimension='COLUMNS'
#     ).execute()
#     pprint(values)


# Пример записи в файл
# values = service.spreadsheets().values().batchUpdate(
#     spreadsheetId=spreadsheet_id,
#     body={
#         "valueInputOption": "USER_ENTERED",
#         "data": [
#             {"range": "B3:C4",
#              "majorDimension": "ROWS",
#              "values": [["This is B3", "This is C3"], ["This is B4", "This is C4"]]},
#             {"range": "D5:E6",
#              "majorDimension": "COLUMNS",
#              "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
# 	]
#     }
# ).execute()
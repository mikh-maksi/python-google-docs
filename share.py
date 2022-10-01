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
spreadsheet_id = '1c37Koz0H0sonZ8vBNTxWdIoTZpJyqP2syU6ykFa3Px8'

# 1ZVIdm4fUrf-1mJIPVw1nem9f6fGcXScLZ9xZ8ZH86Ck
# 1QHdENZb91-V_xRqil3DATRlKshHvhYfKQVds4LweoNw

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

file_id = spreadsheet_id
spreadsheetId = spreadsheet_id


title = 'ASPIRIn - Docs'

spreadsheet = {
    'properties': {
        'title': title
    }
}
spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                            fields='spreadsheetId').execute()
        
new_sheet_id = format(spreadsheet.get('spreadsheetId'))
print(new_sheet_id)


driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
access = driveService.permissions().create(
    fileId = new_sheet_id,
    body = {'type': 'user', 'role': 'writer', 'emailAddress': 'mikhail_maksimov@goit.ua'},  # Открываем доступ на редактирование
    fields = 'id'
).execute()

print(access)


# def callback(request_id, response, exception):
#     if exception:
#         # Handle error
#         print (exception)
#     else:
#         print ("Permission Id: %s" % response.get('id'))

# batch = service.new_batch_http_request(callback=callback)
# user_permission = {
#     'type': 'user',
#     'role': 'writer',
#     'emailAddress': 'mikhail_maksimov@goit.ua'
# }
# batch.add(service.permissions().create(
#         fileId=file_id,
#         body=user_permission,
#         fields='id',
# ))

# domain_permission = {
#     'type': 'domain',
#     'role': 'reader',
#     'domain': 'example.com'
# }
# batch.add(drive_service.permissions().create(
#         fileId=file_id,
#         body=domain_permission,
#         fields='id',
# ))
# batch.execute()
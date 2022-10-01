from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

#   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
#   pip install --upgrade httplib2

# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = '/Users/mac/Documents/work/python/python-google-docs/creds.json'

# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1OjF3c9YomRS6StztlGOFqaYGIKujOhmPB5v0MutJJBQ'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

# Пример чтения файла
values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='F2:F5',
    majorDimension='COLUMNS'
).execute()

right_answers = ['1','2','3','3']
get_answers = values['values'][0]
answers_out = []

for i in range(len(right_answers)):
    if get_answers[i] == right_answers[i]:
        answers_out.append('Правильно')
    else: 
        answers_out.append('Не правильно')

print(get_answers)
print(answers_out)

values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "I2:I5",
             "majorDimension": "COLUMNS",
             "values": [answers_out]}             
	]
    }
).execute()
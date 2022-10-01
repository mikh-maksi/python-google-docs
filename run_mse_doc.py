from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


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
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

# sheet_lst = ['Аналіз','Стратегія','Продукт','Інтелектуальний аналіз продукту','Ресурси','Індікація']

# for sheet in sheet_lst: 
#     values = service.spreadsheets().values().get(
#         spreadsheetId=spreadsheet_id,
#         range=f"'{sheet}'!A2:B12",
#         majorDimension='COLUMNS'
#     ).execute()
#     pprint(values)


sheet = 'Аналіз'

values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f"'{sheet}'!B2:B12",
        majorDimension='COLUMNS'
    ).execute()

# print(values[0][0])

pprint(len(values['values'][0][0]))
for el in values['values'][0]:
    print(len(el))
# print(values.values[0][0])
from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

def avg(lst):
    return sum(lst)/len(lst)

def digit_list(lst):
    digit_lst = []
    for elem in lst:
        if elem == '':
            elem = '0'
        digit_elem = int(elem)
        # digit_elem = 0
        digit_lst.append(digit_elem)
    print(digit_lst)
    return digit_lst
    



# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = '/Users/mac/Documents/work/python/python-google-docs/creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1U-XTzMuPmPvBVHotxrA7mZVvvQ2gdc93d5LL37vPu0o'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

users_lst = ['Кучеренко','Сибиль','Рябищук','Ганноченко','Сютов','Самойленко','Губин']

# Пример чтения файла

n = 3
for user in users_lst: 
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f"'{user}'!B19:J25",
        majorDimension='COLUMNS'
    ).execute()
    # pprint(values)
    lst_out = []
    lst_out.append(user)

    for el in values["values"]:
        int_elem=digit_list(el)
        lst_out.append(sum(int_elem))
    # print(int_elem)
        # print(sum(int_elem))
        # print(avg(int_elem))
    
    print(lst_out)
    values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": f"autoresult!A{n}:J{n}",
             "majorDimension": "ROWS",
             "values": [lst_out]},
	]
    }
    ).execute()
    n = n+1


# values = service.spreadsheets().values().get(
#     spreadsheetId=spreadsheet_id,
#     range="'Кучеренко'!B19:J25",
#     majorDimension='COLUMNS'
# ).execute()
# pprint(values)




print(lst_out)


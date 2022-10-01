from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = '/Users/mac/Documents/work/python/python-google-docs/creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1vHCQW-s8srFi97VKf-v-IuqywEbfZ_6sbzU5agw6ZNo'

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
    range='A1:R1',
    majorDimension='COLUMNS'
).execute()
pprint(values)

dict_elems = ['time','understad','a','s','p','i','r','i','n','n_staff','anual_turnover','name','phone','kved','level']
dict1=dict.fromkeys(dict_elems)
print(dict1)


lst=['time','understad','s','p','i','r','i','n_staff','anual_turnover','name','phone','','n','','a','kved','level']
dict_list = []


# values = service.spreadsheets().values().get(
# spreadsheetId=spreadsheet_id,
# range=f"A2:R2",
# majorDimension='COLUMNS').execute()

for i in range(43):
    # print(i)
    k = i+2
    values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range=f"A{k}:R{k}",
    majorDimension='COLUMNS'
    ).execute()
    # print(values["values"][9])

    for j in range(len(values["values"])):
        el = values["values"][j]
        # print(f"{i} - {el}")
        index = lst[j]
        # print(index)
        if index  == '':
            continue
        dict1[index] = el[0]
        
    # print(dict1)
    dict_list.append(dict1)

print(len(dict_list))

# for elem1 in dict_list:
#     print(elem1)




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
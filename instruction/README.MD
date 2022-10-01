# Робота із API Google stylesheet.
Для початку роботи із Google Stylesheet треба зареєструватися в <a href = "https://console.cloud.google.com/" tagret = "_blank">Google Developer Console</a>
<img src ="img/stylesheet01.png">  
<img src ="img/stylesheet02.png">  
<img src ="img/stylesheet04.png">  
<img src ="img/stylesheet05.png">  
<img src ="img/stylesheet06.png">  
<img src ="img/stylesheet07.png">  
<img src ="img/stylesheet08.png">  
<img src ="img/stylesheet09.png">  
<img src ="img/stylesheet10.png">  
<img src ="img/stylesheet11.png">  
<img src ="img/stylesheet12.png">  
<img src ="img/stylesheet13.png">  
<img src ="img/stylesheet16.png">  
<img src ="img/stylesheet17.png">  
<img src ="img/stylesheet18.png">  
<img src ="img/stylesheet19.png">  
<img src ="img/stylesheet20.png">  

## Внесення значень ячійок в електорнній таблиці
1. Створимо новий документ.

<img src ="img/stylesheet21.png">  
<img src ="img/stylesheet22.png">  

2. Змінимо назву документу
<img src ="img/stylesheet23.png">  

3. Відкриємо доступ до документа
<img src ="img/stylesheet24.png">  
<img src ="img/stylesheet25.png">  
<img src ="img/stylesheet26.png">  

4. Отримаємо ідентифікатор
<img src ="img/stylesheet27.png">  

5. Робимо посилання на файл, підставляємо ідентифікатор
<img src ="img/stylesheet28.png">  

```python

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


# Посилання на файл, полученный в Google Developer Console
CREDENTIALS_FILE = '/Users/mac/Documents/work/python/python-google-docs/instruction/code/stylesheet-project-7742b9ca75f4.json'

# ID Google Sheets документа (його беремо в URL)
spreadsheet_id = '1itYUFazDz9Y76w-t1WnY5HPTXn1HzyXPAL8EvMneZW8'

# Авторизуємося и та отримаємо service — екзепляр доступу до API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

# Задаємо команду, котора в проміжок A1:A2 додає значення "Ячійка А1" та "Ячійка A2" та виконуємо
values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "A1:A2",
             "majorDimension": "COLUMNS",
             "values": [["Ячійка А1","Ячійка A2"]]}  
	]
    }
).execute()

```

6. Запускаємо файл та отримаємо результати

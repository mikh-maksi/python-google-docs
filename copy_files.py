from Google import Create_Service

CLIENT_SECRET_FILE = '/Users/mac/Documents/work/python/python-google-docs/client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)



source_file_id = "1ImhbHmnmp3X504NHE4CIY90TUBmPKlnw"
folder_ids = ['1VWbyfFhi_3ueZLE43irYgwkmWfLJcLgY']

file_metadata = {
    'name' : 'ASPIRIn - document',
    'parents':folder_ids,
    'starred': True,
    'description':'Document for analysis of business'
}
service.files().copy(
    fileId=source_file_id,
    body = file_metadata
).execute()

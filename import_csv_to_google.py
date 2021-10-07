import gspread
from google.oauth2 import service_account
from main import SERVICE_ACCOUNT_FILE, SCOPES, key
import csv


credentials=service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(credentials)

gc = gspread.service_account(filename='meteors_client_secret.json')
sh = gc.open_by_key(key)
SheetName = "Main_data"

sh.values_update(
    SheetName,
    params={'valueInputOption': 'USER_ENTERED'},
    body={'values': list(csv.reader(open("csv_meteor_file.csv", encoding='utf-8')))}
)


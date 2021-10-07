from googleapiclient.discovery import build
from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = "meteors_client_secret.json"
SCOPES = ["https://spreadsheets.google.com/feeds",
          'https://www.googleapis.com/auth/spreadsheets',
          "https://www.googleapis.com/auth/drive.file",
          "https://www.googleapis.com/auth/drive",
          "https://www.googleapis.com/auth/drive.appdata"]

creds = None
creds =service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)

key = '1HmdwjLQJNz6qYt7j5eyWGEypnpa-atHqbBMwFnQ0re4'





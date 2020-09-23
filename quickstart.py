import gspread
from google.oauth2.service_account import Credentials


# Authorize by credentials
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
credentials = Credentials.from_service_account_file(
    'credential_key.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)


# Connect by ID of spreadsheets
sh = gc.open_by_key('1JXU2r0vqKc6tt93B20A_MFRqBJxp9blXUMaD8f1KiwQ')

# Open by worksheet name
worksheet = sh.worksheet("T3")

# Export
print(worksheet)




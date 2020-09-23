import gspread
from google.oauth2.service_account import Credentials
import json
from data_tram import DataTram
from check_value import checkNull

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
# https://docs.google.com/spreadsheets/d/1JXU2r0vqKc6tt93B20A_MFRqBJxp9blXUMaD8f1KiwQ/edit#gid=0
sh = gc.open_by_key('1JXU2r0vqKc6tt93B20A_MFRqBJxp9blXUMaD8f1KiwQ')

# Open by worksheet name
worksheet = sh.worksheet("T3")

# Getting a Cell Value
thangBaoCao = worksheet.acell('Q5').value
namBaoCao = worksheet.acell('S5').value

# Getting a Cell Value
thangBaoCao = worksheet.acell('Q5').value
namBaoCao = worksheet.acell('S5').value

# Getting a Range Value
range_data = worksheet.get('A6:AG28', major_dimension='COLUMNS')

# Get all values from the first row
row6 = worksheet.row_values(6)
danhsachNgay = row6[2:]

row8 = worksheet.row_values(8)
danhsachGiaTri = row8[2:]

dulieu_theongay = {}


for ngay, giatri in zip(danhsachNgay, danhsachGiaTri):
    dulieu_theongay[ngay] = checkNull(giatri)

tentram = range_data[1][2]

# get data
data_tram = DataTram(tentram, namBaoCao, thangBaoCao, dulieu_theongay)
print(data_tram.ten)
print(data_tram.nam_baocao)
print(data_tram.thang_baocao)
print(data_tram.danhsach_giatri_theongay)




# write data
rs = json.dumps(range_data, sort_keys=True, indent=4)
f = open("result.json", "w")
f.write(rs)
f.close()

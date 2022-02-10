import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from pprint import pprint
import pytz
import locale
import sys
import process
sys.path.insert(0,'./process.py')

#set locale
locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')

#Set up credentials
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

#Open gsheet
sa = client.open("Copy of Absensi CBP 2022")
now = datetime.now()
localtz = pytz.timezone('Asia/Jakarta')
date_jkt = int(localtz.localize(now).strftime("%d"))
month_jkt = localtz.localize(now).strftime("%B")
wks = sa.worksheet(month_jkt)

#Get all data
values=wks.get_all_values()
absen=values[2:]

hasil = process.yang_masuk(absen)
import gspread
from pprint import pprint
from datetime import date

sa = gspread.service_account(filename='authentic-reach-302014-a50b679e820e.json')

sh = sa.open("Miro's Scoreboard")

wks = sh.worksheet('April')

# pprint(wks.get("A4:J34"))
today = date.today().strftime("%d.%m.%Y")
row_today = wks.find(today).row
col_today = wks.find(today).col

# Studying Col
def update_today(col, value):
    wks.update_cell(row_today, col, value)
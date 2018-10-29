import json
import openpyxl as xl

wb = xl.load_workbook('Player Stats.xlsx')
ws = wb.active

ws['A1']=("tyber-6832")
wb.save('Player Stats.xlsx')
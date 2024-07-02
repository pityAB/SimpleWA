import pywhatkit
import pyautogui
import time

# import os
import openpyxl

with open('template.txt', 'r') as data_file:
    data = data_file.read()
    # print(data) # test kontent template.txt
textnya=data

# Baca file Excel bernama "data.xlsx"
wb = openpyxl.load_workbook("nomer_siswa.xlsx")
ws = wb.active

nomor=ws["C"]

# datanya=[]

for nom in nomor:
    # pywhatkit.sendwhatmsg(nom,f'{textnya}',14,23)
    cell=nom.value
    print(cell)
    pywhatkit.sendwhatmsg_instantly(f'{cell}',f'{textnya}')
    

# pywhatkit.sendwhatmsg("+6289607860492",f'{textnya}',14,1)
# pywhatkit.sendwhatmsg("+6281227221208",f'{textnya}',14,2)
# pywhatkit.sendwhatmsg("+6281804498543",f'{textnya}',14,3)
# pywhatkit.sendwhatmsg("+6281567824476",f'{textnya}',14,4)
# pywhatkit.sendwhatmsg("+6282137351996",f'{textnya}',14,5)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.press('enter')
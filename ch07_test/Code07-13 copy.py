# tkinter와 xlsxwriter 모듈을 불러옴
from tkinter import *
import xlsxwriter

# Tkinter에서 PhotoImage를 이용하여 이미지를 불러옴
window = Tk()
photo = PhotoImage(file = 'C:/CookAnalysis/GIF2/picture06.gif')

# 이미지의 높이와 너비를 구함
h = photo.height()
w = photo.width()

# 이미지의 각 픽셀의 R, G, B 값을 저장할 리스트 생성
photoR=[ [0 for _ in range(h)] for _ in range(w)]
photoG=[ [0 for _ in range(h)] for _ in range(w)]
photoB=[ [0 for _ in range(h)] for _ in range(w)]

# 이미지의 각 픽셀의 R, G, B 값을 추출하여 리스트에 저장
for i in range(w) :
    for k in range(h) :
        r, g, b = photo.get(i,k)
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b

# 새로운 Excel 파일 생성 및 RGB 시트 생성
workbook = xlsxwriter.Workbook('C:/CookAnalysis/Excel/picture06_art-rgb.xlsx')
worksheet = workbook.add_worksheet('photoRGB')

# R, G, B 값을 각각 시트에 저장
for i in range(w) :
    for k in range(h) :
        worksheet.write(k, i, photoR[i][k])
        worksheet.write(k, i+w, photoG[i][k])
        worksheet.write(k, i+w+w, photoB[i][k])

# 시트의 너비와 높이 설정
worksheet.set_column(0, w - 1, 1.0)  # 약 0.34
for i in range(h):
    worksheet.set_row(i, 9.5)  # 약 0.35

# 각 픽셀의 R, G, B 값을 이용하여 셀의 배경색을 설정하여 시각화
for i in range(w) :
    for k in range(h) :
        hexR = hex(photoR[i][k])
        hexG = hex(photoG[i][k])
        hexB = hex(photoB[i][k])
        hexStr = '#'
        if len(hexR[2:]) < 2:
            hexStr += '0' + hexR[2:]
        else:
            hexStr += hexR[2:]
        if len(hexG[2:]) < 2:
            hexStr += '0' + hexG[2:]
        else:
            hexStr += hexG[2:]
        if len(hexB[2:]) < 2:
            hexStr += '0' + hexB[2:]
        else:
            hexStr += hexB[2:]

        # 각 셀의 배경색 설정
        cell_format = workbook.add_format()
        cell_format.set_bg_color(hexStr)
        worksheet.write(k

from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
def func_open() :
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*"))) 
    photo = PhotoImage(file = filename)
    print("사진의 크기 가로 세로 크기 : %d x %d" %(photo.width(), photo.height()))
    print("사진의 0,0 의 좌표의 RGB 값을 튜플로 보자. :" )
    print(photo.get(0,0))
    # 원본 사진을 좌측에 출력
    pLabel.configure(image = photo)
    pLabel.image = photo
    # 회색 사진을 우측
    photo2 = PhotoImage(file = filename)
    photo2 = photo.subsample(1, 1)
    for i in range(0, photo2.width()) :
        for k in range(0, photo2.height()) :
            r, g, b = photo2.get(i, k)
            grey = int((r + g + b) / 3)
            photo2.put("#%02x%02x%02x" % (grey, grey, grey), (i, k))
    print(photo2.get(0,0))
    pLabel2.configure(image = photo2)
    pLabel2.image = photo2
    
def func_exit() :
    window.quit()
    window.destroy()

## 메인 코드  부분 ##
window = Tk()
window.geometry("500x500")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(side=LEFT)
photo2 = PhotoImage()
pLabel2 = Label(window, image = photo2)
pLabel2.pack(side=RIGHT)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

window.mainloop()

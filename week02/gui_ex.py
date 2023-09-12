import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()

def simple_gui_input(text="값을 입력하세요"):
    return simpledialog.askstring(title="TEST",
                                  prompt=text)

if __name__=="__main__":
    user_input = simple_gui_input("첫번째 숫자를 입력해주세요")
    user_input2 = simple_gui_input("두번째 숫자를 입력해주세요")


    print(f"입력된 값은 {user_input}, {user_input2} 입니다")



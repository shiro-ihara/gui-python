import tkinter as tk
from tkinter import filedialog
def sub_window():
    # サブウインドウの作成
    about_window = tk.Toplevel(root)
    about_window.geometry("200x100") 

def set_func():
    typ=[("GAMESS","*.txt")]
    file_path=filedialog.askopenfilename(filetypes=typ)
    input_box.delete(0,tk.END)
    input_box.insert(tk.END,file_path)

def run_func():
    sub_window()
    with open(input_box.get(),"r") as outfile:
        data=outfile.readlines()

    for linenum,line in enumerate(data):
        if "LOCATED" in line:
            finalnum=linenum
    words=data[(finalnum+4):]

    with open("xyz.txt","w+") as datafile:
        for line in words:
            if line == "\n":
                break
            else:
                datafile.write(line)
    statusbar["text"]="Done!!"
def quit():
    if tk.messagebox.askyesno("確認", "終了しますか？"):
        root.destroy()
def exc_run_func():
    try:
        run_func()
    except:
        statusbar["text"]="Error!!"
root=tk.Tk()
root.geometry("350x100")
root.title("Test")
#root.iconphoto(True,tk.PhotoImage(file=""))
root.resizable(width=False,height=False)

# メニューバーの作成
menubar = tk.Menu(root)
root.configure(menu = menubar)
# ファイルメニュー
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
# ～内容
filemenu.add_command(label = "Open File...")
# セパレーター
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = lambda: root.destroy())

run_button=tk.Button(root,text="Run",command=exc_run_func)
run_button.place(x=160,y=40)

set_button=tk.Button(root,text="Set",command=set_func)
set_button.place(x=300,y=7)

quit_button=tk.Button(root,text="Quit",command=quit)
quit_button.place(x=300,y=40)

input_box=tk.Entry(width=40)
input_box.place(x=10,y=10)

#bd = 1 ：縁(ボーダー)の幅を1に指定 (値を大きくすると幅が広がります)
#relief = tk.SUNKEN： 縁のスタイルを指定 (SUNKEN：親要素より沈んで表示)
#anchor = tk.W： 配置可能なスペースに余裕がある場合、ウイジットをどこに配置するか指定 (W ：左よせ)
statusbar=tk.Label(root,text="No data!!",bd=1,relief=tk.SUNKEN,anchor=tk.W)
statusbar.place(x=10, y=75)
root.mainloop()
print("abc")
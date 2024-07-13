# working institution:School of Mathematical Sciences,Zhejiang University
# author:Kangjie Ding
# date:2024/5/17 10:18
import os
import time
import tkinter as tk
from data_generator import data_generate, data_process
from datetime import date
from pathlib import Path
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog, ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widget()

    def create_widget(self):
        """
        创建组件
        """
        # 用label表示的图片，作为程序背景
        canvas = tk.Canvas(self, width=800, height=400)
        img = Image.open("tobaccos.png")
        global photo
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(400, 250, image=photo)
        canvas.pack()
        # # 标签组件
        # self.label1 = tk.Label(self, text="请输入植株数量")
        # self.label1.place(x=350, y=0)
        # # 文本框组件
        # plant_num = tk.StringVar()
        # self.entry1 = tk.Entry(self, textvariable=plant_num)
        # self.entry1.place(x=320, y=20)
        # # 按钮组件，用来生成指定数据
        # tk.Button(self, text="生成数据", command=self._generate).place(x=365, y=45)

        # 按钮组件，用来执行选择文件指令
        tk.Button(self, text="请选择存放原始植株数据的文件夹", command=self._select_folder).place(x=270, y=60)
        self.entry2 = tk.Entry(self, width=50)
        self.entry2.place(x=200, y=95)
        # 按钮文件，用来对原始批量植株数据做预处理
        tk.Button(self, text="数据预处理", command=self._preprocess).place(x=310, y=115)
        # 标签组件
        self.label2 = tk.Label(self, text="请选择需要生成哪些数据")
        self.label2.place(x=200, y=150)
        # 复选框设置
        self.checkVar1 = tk.IntVar()
        self.checkVar2 = tk.IntVar()
        self.checkVar3 = tk.IntVar()
        self.checkVar4 = tk.IntVar()
        self.check1 = tk.Checkbutton(self, text="株高", variable=self.checkVar1, onvalue=1, offvalue=0)
        self.check2 = tk.Checkbutton(self, text="叶片数", variable=self.checkVar2, onvalue=1, offvalue=0)
        self.check3 = tk.Checkbutton(self, text="叶面积", variable=self.checkVar3, onvalue=1, offvalue=0)
        self.check4 = tk.Checkbutton(self, text="叶夹角", variable=self.checkVar4, onvalue=1, offvalue=0)
        self.check1.place(x=270, y=175)
        self.check2.place(x=340, y=175)
        self.check3.place(x=410, y=175)
        self.check4.place(x=480, y=175)
        # 按钮组件，根据复选框内容进行响应
        tk.Button(self, text="处理数据", command=self._process_data).place(x=290, y=205)
        # 退出程序按钮
        tk.Button(self, text="退出", command=self.master.destroy).place(x=360, y=205)

    # def _generate(self):
    #     plant_num = int(self.entry1.get())
    #     data_generate(plant_num)
    #     messagebox.showinfo("提示", "成功生成植株数据！")

    def _select_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.foldername = str(Path(folder_selected))
        self.entry2.delete(0, tk.END)
        self.entry2.insert(0, self.foldername)

    def _preprocess(self):
        """批量数据预处理，筛选出合格植株数据存放到临时文件夹，方便后续处理"""
        files = [os.path.join(self.foldername, filename) for filename in
                 os.listdir(self.foldername)]
        if files[0].split(".")[-1] != "TXT":
            messagebox.showwarning("警告", "原始数据存储格式不符合要求！")
            return
        today = date.today().strftime("%Y-%m-%d")
        processed_data_date = "processed_data-"+today
        if processed_data_date not in os.listdir(os.getcwd()):
            os.mkdir(processed_data_date)

        # 设置弹窗
        popup = tk.Toplevel(self.master)
        popup.title("数据预处理中")
        popup.geometry("250x100")
        popup.attributes("-topmost", 1)
        # 设置弹窗上的进度条
        progress_var = tk.DoubleVar()
        progress_bar = ttk.Progressbar(popup, length=200, variable=progress_var, mode="determinate")
        progress_bar.place(x=10, y=30)

        for i, file in enumerate(files):
            data_process(file, processed_data_date)
            progress_var.set(int(200/len(files)*i))
            popup.update()
            time.sleep(0.5)
        # 进度完成后关闭弹窗
        popup.destroy()
        time.sleep(0.5)
        messagebox.showinfo("提示", "成功完成数据预处理")

    def _process_data(self):
        flags = [self.checkVar1.get(), self.checkVar2.get(), self.checkVar3.get(), self.checkVar4.get()]
        s = ""
        if flags[0]:
            s += "{株高}"
        if flags[1]:
            s += "{叶片数}"
        if flags[2]:
            s += "{叶面积}"
        if flags[3]:
            s += "{叶夹角}"
        messagebox.showinfo("提示", f"成功生成{s}统计数据")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("这是一个生成植株数据的简单Gui程序")
    window.geometry("800x400+200+100")
    # 设置ico图标
    window.iconbitmap("tobacco.ico")
    app = Application(master=window)

    window.mainloop()


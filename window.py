# working institution:School of Mathematical Sciences,Zhejiang University
# author:Kangjie Ding
# date:2024/5/17 10:18
import tkinter as tk
from tkinter import messagebox, filedialog
from data_generator import data_generate, data_process
from PIL import ImageTk, Image


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
        # 用label表示的图片
        canvas = tk.Canvas(self, width=800, height=400)
        img = Image.open("tobaccos.png")
        global photo
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(400, 250, image=photo)
        canvas.pack()
        # 标签组件
        self.label1 = tk.Label(self, text="请输入植株数量")
        self.label1.place(x=350, y=0)
        # 文本框组件
        plant_num = tk.StringVar()
        self.entry1 = tk.Entry(self, textvariable=plant_num)
        self.entry1.place(x=320, y=20)
        # 按钮组件，用来生成指定数据
        tk.Button(self, text="生成数据", command=self._generate).place(x=365, y=45)
        # 按钮组件，用来执行选择文件指令
        tk.Button(self, text="选择文件", command=self._select_file).place(x=250, y=80)
        tk.Button(self, text="处理数据", command=self._process_data).place(x=250, y=110)
        self.entry2 = tk.Entry(self, width=50)
        self.entry2.place(x=310, y=85)

    def _generate(self):
        plant_num = int(self.entry1.get())
        data_generate(plant_num)
        messagebox.showinfo("提示", "成功生成植株数据！")

    def _select_file(self):
        filetypes = (('text files', '*.txt'), ('comma separated file', '*.csv'),
                     ('All files', '*.*'))
        self.filename = filedialog.askopenfilename(title='Open a file', initialdir='/',
                                              filetypes=filetypes)
        self.entry2.delete(0, tk.END)
        self.entry2.insert(0, self.filename)

    def _process_data(self):
        data_process(self.filename)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("这是一个生成植株数据的简单Gui程序")
    window.geometry("800x400+200+100")
    # 设置ico图标
    window.iconbitmap("tobacco.ico")
    app = Application(master=window)

    window.mainloop()


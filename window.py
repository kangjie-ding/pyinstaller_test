# working institution:School of Mathematical Sciences,Zhejiang University
# author:Kangjie Ding
# date:2024/5/17 10:18
import tkinter as tk
from tkinter import messagebox, filedialog
from data_generator import data_generate


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
        # 标签组件
        self.label1 = tk.Label(self, text="请输入植株数量")
        self.label1.pack()
        # 文本框组件
        plant_num = tk.StringVar()
        self.entry1 = tk.Entry(self, textvariable=plant_num)
        self.entry1.pack()
        # 按钮组件，用来生成指定数据
        tk.Button(self, text="生成数据", command=self._generate).pack()
        # 按钮组件，用来执行选择文件指令
        tk.Button(self, text="选择文件", command=self._select_file).pack(side=tk.LEFT)
        self.entry2 = tk.Entry(self, width=50)
        self.entry2.pack(side=tk.LEFT)

    def _generate(self):
        plant_num = int(self.entry1.get())
        data_generate(plant_num)
        messagebox.showinfo("提示", "成功生成植株数据！")

    def _select_file(self):
        filetypes = (('text files', '*.txt'), ('comma separated file', '*.csv'),
                     ('All files', '*.*'))
        filename = filedialog.askopenfilename(title='Open a file', initialdir='/',
                                              filetypes=filetypes)
        # 可以在这里加入处理文件“filename”的代码
        self.entry2.delete(0, tk.END)
        self.entry2.insert(0, filename)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("这是一个生成植株数据的简单Gui程序")
    window.geometry("800x400+200+100")
    app = Application(master=window)

    window.mainloop()


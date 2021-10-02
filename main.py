import os.path
import shutil
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import messagebox
from tkinter import font

import cv2


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.video_file_path = tk.StringVar()
        self.pic_dir_path = tk.StringVar()
        self.interval = tk.StringVar(value="10")
        self.btn_text = tk.StringVar(value="")
        # 设置窗口大小
        master.geometry('520x180')
        master.title("视频抽帧")
        self.initial_frame()

    def initial_frame(self):
        video_file_frame = Frame(self)
        Label(video_file_frame, text="请选择视频文件：", width=14, anchor="e").grid(row=0, column=0, padx=3)
        Button(video_file_frame, text="请选择...", command=self.select_video_file).grid(row=0, column=1)

        dir_path_frame = Frame(self)
        Label(dir_path_frame, text="请选择图片存储路径：", width=14, anchor="e").grid(row=1, column=0, padx=3)
        Button(dir_path_frame, text="请选择...", command=self.select_pic_dir).grid(row=1, column=1)

        video_file_frame.grid(pady=6)
        dir_path_frame.grid(pady=6)

        tips_frame = Frame(self)
        Label(tips_frame, text="输入图片保存的间隔：", width=16, anchor="e").grid(row=1, column=0)
        Entry(tips_frame, text=self.interval, width=8).grid(row=1, column=1)
        tips_frame.grid(pady=6)

        Button(self, text="开始抽帧", command=self.start_frame_draw).grid(pady=6)
        Label(self, textvariable=self.btn_text, fg="red", font=font.Font(size=16)).grid(pady=6)

    # 选择视频文件方法
    def select_video_file(self):
        self.video_file_path = askopenfilename(title=u'选择视频文件')
        file_name_lists = str(self.video_file_path).split("/")
        messagebox.showinfo("文件提示", "选择的文件为 %s" % list(file_name_lists)[-1])

    # 选择文件夹
    def select_pic_dir(self):
        self.pic_dir_path = askdirectory(title=u'选择图片存放路径')
        messagebox.showinfo("目录提示", "选择的存储目录为 %s" % self.pic_dir_path)

    # 开始抽帧程序
    def start_frame_draw(self):
        interval = str(self.interval.get())
        video_file = str(self.video_file_path)
        pic_dir_path = str(self.pic_dir_path)
        if len(video_file) == 0:
            messagebox.showerror("警告", "还没有选择视频文件")
            return

        if len(pic_dir_path) == 0:
            messagebox.showerror("警告", "还没有选择图片的存放路径")
            return

        if len(interval) == 0:
            messagebox.showerror("警告", "你还没有输入视频抽帧的间隔")
            return

        self.btn_text.set("抽帧中...")
        self.get_video_frame(video_file, pic_dir_path, interval)

    def get_video_frame(self, video_path, dir_path, interval):
        # 获取视频名称
        video_name = video_path.split("/")[-1].split(".")[0]
        is_exists = os.path.exists(dir_path)
        if not is_exists:
            os.makedirs(dir_path)
        else:
            shutil.rmtree(dir_path)
            os.makedirs(dir_path)

        video_capture = cv2.VideoCapture(video_path)
        i = 0
        count = 0
        while True:
            success, frame = video_capture.read()
            i += 1
            if i % int(interval) == 0:
                count += 1
                pic_path = dir_path + "/" + video_name + "_" + str(i) + ".jpg"
                cv2.imwrite(pic_path, frame)
            if not success:
                self.btn_text.set("程序已完成抽帧，请前往目录查看")
                break


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

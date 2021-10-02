# 视频抽帧程序

采用Python + Tkinter + CV2 开发简易版的视频抽帧程序，可根据设置抽帧的间隔进行对视频进行抽帧

### 环境要求

- Python 3.6或以上
- cv2

### 软件打包

首先需要安装 `pyinstaller`

> 安装依赖
```shell
$ pip install pyinstaller
```

在根目录下执行以下命令进行打包：
```shell
pyinstaller -F -w main.py
```

`-F`表示打包一个该系统所执行的程序，`-w`表示仅窗口，无控制台

打包好的程序位于 `dist` 目录下


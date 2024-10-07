# 初始化插件
import sys
import tkinter as tk
from tkinter import messagebox
import time
import webbrowser
# 定义全局变量
species = 0
DSL = 0
try:
# 定义日志函数
    def log(msg):
        print(msg)
    # 定义错误、警告、信息、调试日志函数
    def error(msg):
        print("Error: " + msg)
    def warning(msg):
        print("Warning: " + msg)
    def info(msg):
        print("Info: " + msg)
    def debug():
        debugis()
    log("初始化插件A0区...OK")
    DSL = DSL + 1
except Exception as e:
    print("初始化插件A0区...失败")
# 定义时间函数
time.time()
AOK = 0
# 定义全局变量
Window = None
try:
    # 创建窗口
    window = tk.Tk()
    window.x = "500"
    window.y = "500"
    window.resizable(False, False)
    window.geometry("865x540")
    window.title("Game")
    # 初始化图标
    window.iconbitmap("Gamedata/icon/Game-ico.ico")
    # 提前定义
    botQ1 = None
    lab = tk.Label(window, text="沃的厨房", bg="white", font=("Arial", 10), width=15, height=7)
    if DSL == 4:
        print("初始化成功！")
    # 生成游戏标签
    lab.pack()
    # 提前定义
    botQ2 = None
    # 提前定义
    botQ3 = None
    # 提前定义
    botQ4 = None
    # 提前定义
    botQ5 = None
    # 提前定义
    botQ6 = None
    # 提前定义
    botQ7 = None
    BA = "0"
    # 提前定义
    botKS1 = None
    # 设置窗口大小
    window.geometry("865x540")
    # 提前定义
    SD = None
    # 提前定义
    GameWindow = None
    # 方法定义
    DSL = DSL + 1
    log("初始化插件A1区...OK")
except Exception as e:
    print("初始化插件A1区...失败")
# 游戏加载检测
def GameLoadWhat():
    messagebox.showerror("Error", "游戏加载失败！\n请联系游戏作者") # 弹出错误提示框
def GameStart():
    def NOGAME():
        window.deiconify() # 显示窗口
        GameWindow.destroy() # 销毁游戏窗口
    # 创建游戏窗口
    global GameWindow # 声明全局变量
    messagebox.askquestion(title="游戏开始",message="游戏开始！\n按任意键继续,按Delete键退出游戏 按F11全屏") # 弹出提示框
    window.withdraw() # 隐藏窗口
    GameWindow = tk.Toplevel(window, width=1200, height=600, bg="honeydew") # 创建游戏窗口
    GameWindow.title("游戏窗口") # 设置游戏窗口的标题
    GameWindow.bind("<F11>", lambda e: attributesNo2()) # 绑定F11全屏
    GameWindow.bind("<Delete>", lambda e: NOGAME()) # 绑定Delete退出全屏 绑定Esc退出全屏
    GameWindow.resizable(False, False) # 设置游戏窗口是否可变
    GameWindow.iconbitmap("Gamedata/icon/playGame.ico") # 设置游戏窗口的图标
    GameWindow.geometry("1200x600")  # 设置游戏窗口的大小
    # 定义游戏窗口的布局
    GameWindow.grid_columnconfigure(0, weight=1)  # 设置游戏窗口的列权重
    GameWindow.grid_rowconfigure(0, weight=1)  # 设置游戏窗口的行权重
    GameWindow.mainloop() # 进入游戏窗口
# 创建赞助窗口
def create_child_window():
    # 创建一个Toplevel窗口作为子窗口
    child_window = tk.Toplevel(window)  # 创建子窗口
    # 初始化图标
    child_window.iconbitmap("Gamedata/icon/goodGame.ico")  # 设置子窗口的图标
    child_window.title("赞助窗口")  # 设置子窗口的标题
    child_window.geometry("600x150")  # 设置子窗口的大小
    # 在子窗口中添加一个标签
    label = tk.Label(child_window, text="输入Warma(视频创作者)或dideng(游戏作者)以打开 她/我 的个人主页", font=("Arial", 12))  # 创建标签
    label.pack(pady=10, padx=10) # 生成标签

    # 在子窗口中添加一个输入框
    entry = tk.Entry(child_window, width=30)  # 创建输入框
    entry.pack(pady=5, padx=10)  # 生成输入框

    # 定义一个内部函数来处理按钮点击事件
    def open_webpage_internal():
        # 获取输入框中的内容
        user_inputgood = entry.get()  # 获取输入框的内容

        # 检查输入的内容是否匹配特定的值
        if user_inputgood == "Warma":  # 输入内容匹配
            # 使用webbrowser模块打开网页
            webbrowser.open_new("https://space.bilibili.com/53456") # 打开-W
        elif user_inputgood == "dideng":
            webbrowser.open_new("https://space.bilibili.com/1749090711") # 打开-D
        else:
            # 如果输入不匹配，显示错误消息
            messagebox.showerror("错误", "请输入正确的作者以打开他的个人主页")
    # 按钮
    open_button = tk.Button(child_window, text="确定", command=open_webpage_internal)
    open_button.pack(pady=10, padx=10) # 生成按钮
def load_game():
    messagebox.showwarning("读档", "读档功能暂未开放") # 弹出提示框
    GameLoadWhat() # 弹出错误提示框
def about_button():
    messagebox.showinfo("关于", "沃的厨房\n版本：1.0.0\n游戏作者：dideng\n作者：Warma\n""游戏作者联系方式：3483434955@qq.com") # 弹出提示框
try:
    def debugis():
        global species  # 声明全局变量
        def debugQA():  # Debug按钮点击事件
            if debugbEntey.get() == "/species +X":  # 指令输入有效
                messagebox.showinfo("Debug","指令输入有效，请到cmd（PyCharm）中继续") # 弹出提示框
                JT = input("输入加数\n") # 输入加数
                global species # 声明全局变量
                species = species + int(JT) # 增加金币
                messagebox.showinfo("Debug", "指令执行成功！") # 弹出提示框
                messagebox.showinfo("Debug", "成功增加了"+str(JT)+"金币！ 当前金币：" + str(species)) # 弹出提示框
        debugWindow = tk.Toplevel(window) # 创建Debug窗口
        debugWindow.title("Debug") # 设置Debug窗口的标题
        debugWindow.iconbitmap("Gamedata/icon/debug.ico") # 设置Debug窗口的图标
        debugWindow.geometry("600x300")         # 设置Debug窗口的大小
        debugWindow.resizable(False, False)    # 设置Debug窗口是否可变
        debugWindow.lift()                     # 窗口置顶
        debugWindow.bind("<Delete>", lambda e: debugWindow.destroy()) # 绑定Delete退出Debug窗口
        debugbutton1 = tk.Button(debugWindow, text="退出", width=16, height=1, font=("Arial", 10), command=debugWindow.destroy)  # 创建退出Debug按钮
        debugbutton1.place(relx=0.5, rely=0.91, anchor=tk.CENTER)  # 使用相对位置居中
        label = tk.Label(debugWindow, text="Debug模式", font=("Arial", 12))  # 创建Debug标签
        label.pack(pady=10, padx=10)  # 生成标签
        debugbEntey = tk.Entry(debugWindow, width=30)  # 创建Debug输入框
        debugbEntey.pack(pady=20)    # 生成输入框
        debugbutton2 = tk.Button(debugWindow, text="OK", width=16, height=1, font=("Arial", 10), command=debugQA)  # 创建Debug按钮
        debugbutton2.pack(pady=20)  # 生成按钮
        debugWindow.mainloop()  # 进入Debug窗口
    # 主页按钮
    def hide_button_botQ1():
        global BA, botKS1
        if botQ1 and botQ1.winfo_viewable():  # 按钮可见
            botQ1.place_forget()  # 隐藏按钮
            BA = "1"  # 按钮状态
            if not botKS1:
                botQ1_click() # 开始游戏按钮
                botQ2_click() # 赞助按钮
                botQ3_click() # 关于按钮
                botQ4_click() # 读档按钮
                botQ6_click() # 设置按钮
                botQ5_click() # 退出按钮
    def attributesNo(): # 全屏无边框按钮
        global AOK
        if AOK == 0:
            window.attributes("-fullscreen", True)  # 进入全屏
            AOK = AOK + 1
        elif AOK == 1:
            window.attributes("-fullscreen", False)  # 退出全屏
            AOK = AOK - 1
    def attributesNo2(): # 全屏无边框按钮
        global AOK
        if AOK == 0:
            GameWindow.attributes("-fullscreen", True)  # 进入全屏
            AOK = AOK + 1
        elif AOK == 1:
            GameWindow.attributes("-fullscreen", False)  # 退出全屏
            AOK = AOK - 1
    def botQ1_click():
        global botKS1
        botKS1 = tk.Button(window, text="开始游戏", width=20, height=1, font=("Arial", 10), command=GameStart)  # 创建开始游戏按钮
        botKS1.pack(pady=10)
    def botQ2_click():
        botKS2 = tk.Button(window, text="赞助", width=20, height=1, font=("Arial", 10),command=create_child_window)  # 创建赞助按钮
        botKS2.pack(pady=10)  # 生成按钮
    def botQ3_click():
        botKS3 = tk.Button(window, text="关于", width=20, height=1, font=("Arial", 10), command=about_button)  # 创建关于按钮
        botKS3.pack(pady=10)  # 生成按钮
    def botQ4_click():
        botKS4 = tk.Button(window, text="读档", width=20, height=1, font=("Arial", 10), command=load_game)  # 创建读档按钮
        botKS4.pack(pady=10)  # 生成按钮
    def botQ5_click():
        botKS5 = tk.Button(window, text="退出", width=20, height=1, font=("Arial", 10), command=window.quit)  # 创建退出按钮
        botKS5.pack(pady=10)  # 生成按钮
    def botQ6_click():
        botKS6 = tk.Button(window, text="设置", width=20, height=1, font=("Arial", 10), command=Options)  # 创建全屏无边框按钮
        botKS6.pack(pady=10)  # 生成按钮
    def Options():
        SZ = tk.Toplevel(window)
        SZ.title("设置")
        SZ.iconbitmap("Gamedata/icon/settings.ico")
        SZ.geometry("600x350")
        SZ.resizable(False, False)
        SZ.lift()
        SZ.bind("<Delete>", lambda e: debug())
        button1 = tk.Button(SZ, text="退出", width=16, height=1, font=("Arial", 10), command=SZ.destroy)
        button1.place(relx=0.5, rely=0.91, anchor=tk.CENTER)
        label = tk.Label(SZ, text="全屏模式", font=("Arial", 12))
        label.pack(pady=10, padx=10)
        button2 = tk.Button(SZ, text="全屏无边框", width=15, height=1, font=("Arial", 10), command=attributesNo)
        button2.pack(pady=10, padx=10)
    def OKGame():
        messagebox.askquestion("", "授权成功", icon="info")
        hide_button_botQ1()
    log("初始化函数...OK")
    DSL = DSL + 1
except Exception as e:
    print("初始化函数...失败")
# 显示开始游戏按钮
try:
    result = messagebox.askquestion("", "确定要启动游戏吗？", icon="question")
    if result == "yes":
        messagebox.askquestion("", "请去Game Window进行最后确定", icon="warning") # 弹出提示框
        botQ1 = tk.Button(window, text="确定请求", width=12, height=2, command=OKGame) # 创建开始游戏按钮
        botQ1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # 使用相对位置居中
    else:
        sys.exit()
    log("正常启动...OK")
    DSL = DSL + 1
    if DSL == 4:
        print("初始化成功！")
except Exception as e:
    print("正常启动...失败")
    if DSL == 4:
        print("初始化成功！")
    else:
        print("初始化失败！")
        sys.exit()
    sys.exit()
try:
    # 进入主循环
    window.mainloop()
    log("主循环...OK")
    DSL = DSL + 1
except Exception as e:
    print("主循环...失败")
    sys.exit()
window.mainloop()
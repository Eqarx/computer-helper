import tkinter as tk
import os

def speed_up():
    os.system(os.path.join(os.environ['TEMP'], 'RAM_killer.bat'))

def solve_issues():
    os.system(os.path.join(os.environ['TEMP'], 'blsc.bat'))

# 创建主窗口
root = tk.Tk()
root.title("电脑小助手")

# 设置窗口大小
window_width = 640
window_height = 320
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# 创建标签，显示大号加粗文字
title_label = tk.Label(root, text="电脑小助手", font=("Arial", 64, "bold"))
title_label.pack(pady=20)

# 创建标签，显示小号文字
subtitle_label = tk.Label(root, text="让您的电脑再次伟大！！！", font=("Arial", 20))
subtitle_label.pack()

# 创建按钮，一键提速
speed_up_button = tk.Button(root, text="一键提速", command=speed_up, font=("Arial", 26), height=3, width=13)
speed_up_button.pack(side=tk.LEFT, padx=20)

# 创建按钮，一键解决问题
solve_issues_button = tk.Button(root, text="一键解决问题", command=solve_issues, font=("Arial", 26), height=3, width=13)
solve_issues_button.pack(side=tk.RIGHT, padx=20)

# 定义变色函数
def change_color():
    current_color = title_label.cget("fg")
    next_color = "red" if current_color != "red" else "blue"
    title_label.config(fg=next_color)
    root.after(50, change_color)  # 1秒后再次调用自身

# 开始变色
change_color()

# 运行主循环
root.mainloop()

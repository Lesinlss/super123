import tkinter as tk

# 窗口设置
root = tk.Tk()
root.title("专注时钟")
root.geometry("300x150")

# 定义 countdown 函数
def countdown(count):
    # 从 60 开始倒计时，并更新剩余秒数的标签
    label['text'] = count

    if count > 0:
        # 每秒减少1，使用 after 模块实现倒计时
        root.after(1000, countdown, count-1)
    else:
        # 时间到，弹出提醒窗口
        popup = tk.Toplevel()
        popup.title("时间到！")
        popup.geometry("200x100")
        label_popup = tk.Label(popup, text="休息10分钟!")
        label_popup.pack(fill='x', padx=30, pady=10)
        btn = tk.Button(popup, text="关闭", command=popup.destroy)
        btn.pack(pady=5)

# 开始按钮点击事件逻辑
def start():
    # 清空计数器
    count = 60
    # 调用 countdown 函数
    countdown(count)

# 退出按钮点击事件逻辑
def exit():
    root.destroy()

# 设置开始和退出按钮
start_btn = tk.Button(root, text="开始", command=start)
exit_btn = tk.Button(root, text="退出", command=exit)
start_btn.pack(side='left', padx=10, pady=10)
exit_btn.pack(side='right', padx=10, pady=10)

# 显示剩余秒数的标签
label = tk.Label(root, text="60", font=("Helvetica", 30))
label.pack(pady=10)

# 运行程序
root.mainloop()

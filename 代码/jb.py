import ctypes

# 回调函数
def enum_handler(hwnd, lParam):
    if ctypes.windll.user32.IsWindowVisible(hwnd):
        # 输出窗口标题和句柄
        title = ctypes.create_unicode_buffer(255)
        ctypes.windll.user32.GetWindowTextW(hwnd, title, 255)
        print("窗口标题：", title.value)
        print("句柄：", hwnd)
    return True

# 获取所有程序的句柄
ctypes.windll.user32.EnumWindows(ctypes.PYFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.c_int)(enum_handler), 0)

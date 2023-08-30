from ctypes import windll, byref
from ctypes.wintypes import HWND, POINT
import time

PostMessageW = windll.user32.PostMessageW
ClientToScreen = windll.user32.ClientToScreen
WM_MOUSEMOVE = 0x0200
WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x202
WM_RBUTTONDOWN = 0x0204
WM_RBUTTONUP = 0x0205
WM_MOUSEWHEEL = 0x020A

WHEEL_DELTA = 120


def move_to(hand: HWND, x: int, y: int):
    """移动鼠标到坐标（x, y)

    Args:
        handle (HWND): 窗口句柄
        x (int): 横坐标
        y (int): 纵坐标
    """
    # https://docs.microsoft.com/en-us/windows/win32/inputdev/wm-mousemove
    wparam = 0
    lparam = y << 16 | x
    PostMessageW(hand, WM_MOUSEMOVE, wparam, lparam)


def left_down(hand: HWND, x: int, y: int):
    """在坐标(x, y)按下鼠标左键

    Args:
        handle (HWND): 窗口句柄
        x (int): 横坐标
        y (int): 纵坐标
    """
    # https://docs.microsoft.com/en-us/windows/win32/inputdev/wm-lbuttondown
    wparam = 0
    lparam = y << 16 | x
    PostMessageW(hand, WM_LBUTTONDOWN, wparam, lparam)


def left_up(hand: HWND, x: int, y: int):
    """在坐标(x, y)放开鼠标左键

    Args:
        handle (HWND): 窗口句柄
        x (int): 横坐标
        y (int): 纵坐标
    """
    # https://docs.microsoft.com/en-us/windows/win32/inputdev/wm-lbuttonup
    wparam = 0
    lparam = y << 16 | x
    PostMessageW(hand, WM_LBUTTONUP, wparam, lparam)

def right_down(hand:HWND,x:int,y:int):
    """在坐标(x, y)按下鼠标右键

    Args:
        handle (HWND): 窗口句柄
        x (int): 横坐标
        y (int): 纵坐标
    """
    # https://docs.microsoft.com/en-us/windows/win32/inputdev/wm-rbuttondown
    wparam = 0
    lparam = y << 16 | x
    PostMessageW(hand, WM_RBUTTONDOWN, wparam, lparam)

def right_up(hand:HWND,x:int,y:int):
    """在坐标(x, y)放开鼠标右键

    Args:
        handle (HWND): 窗口句柄
        x (int): 横坐标
        y (int): 纵坐标
    """
    # https://docs.microsoft.com/en-us/windows/win32/inputdev/wm-rbuttonup
    wparam = 0
    lparam = y << 16 | x
    PostMessageW(hand, WM_RBUTTONUP, wparam, lparam)

def scroll(hand: HWND, delta: int, x: int, y: int):
    """在坐标(x, y)滚动鼠标滚轮

    Args:
        handle (HWND): 窗口句柄
        delta (int): 为正向上滚动，为负向下滚动
        x (int): 横坐标
        y (int): 纵坐标
    """
    move_to(hand, x, y)
    # https://docs.microsoft.com/en-us/windows/win32/inputdev/wm-mousewheel
    wparam = delta << 16
    p = POINT(x, y)
    ClientToScreen(hand, byref(p))
    lparam = p.y << 16 | p.x
    PostMessageW(hand, WM_MOUSEWHEEL, wparam, lparam)


def scroll_up(hand: HWND, x: int, y: int):
    """在坐标(x, y)向上滚动鼠标滚轮

    Args:
        handle (HWND): 窗口句柄
        x (int): 横坐标
        y (int): 纵坐标
    """
    scroll(hand, WHEEL_DELTA, x, y)


def scroll_down(hand: HWND, x: int, y: int):
    """在坐标(x, y)向下滚动鼠标滚轮

    Args:
        handle (HWND): 窗口句柄
        x (int): 横坐标
        y (int): 纵坐标
    """
    scroll(hand, -WHEEL_DELTA, x, y)


def click_left(hand:HWND,x:int,y:int):
    """在坐标(x, y)按下鼠标左键后抬起

    Args:
        handle (HWND): 窗口句柄
        x (int): 横坐标
        y (int): 纵坐标
    """
    move_to(hand, x, y)
    left_down(hand,x,y)
    left_up(hand,x,y)


def click_right(hand,x,y):
    """在坐标(x, y)按下鼠标右键后抬起

    Args:
        handle (HWND): 窗口句柄
        x (int): 横坐标
        y (int): 纵坐标
    """
    move_to(hand, x, y)
    right_down(hand,x,y)
    right_up(hand,x,y)




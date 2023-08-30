""" import win32api
import win32con
import win32gui
import time
import win32clipboard as w


def FindWindow(hand):
    win = hand
    
    if win != 0:
        #win32gui.ShowWindow(win, win32con.SW_SHOWMINIMIZED)
        win32gui.ShowWindow(win, win32con.SW_SHOWNORMAL)
        #win32gui.ShowWindow(win, win32con.SW_SHOW)
        #win32gui.SetWindowPos(win, win32con.HWND_TOPMOST, win32con.SWP_SHOWWINDOW)
        try:
            win32gui.SetForegroundWindow(win)  # 获取控制
            print("找到窗口：")
            time.sleep(1)
        except:
            print('不要放在前台2')
    else:
        print('没找到，请激活窗口' )
        exit()

def CloseWindow(hand):
    win = hand
    #print("找到关闭窗口：%x" % win)
    time.sleep(3)
    win32gui.ShowWindow(win, win32con.SW_SHOWMINIMIZED)

def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

def ctrlV():
    win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
    win32api.keybd_event(86,0,0,0)  #v键位码是86
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
 
def altS():
    win32api.keybd_event(18, 0, 0, 0)    #Alt键位码
    win32api.keybd_event(83,0,0,0) #s键位码
    win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0)

def sendText(hand,text):
    FindWindow(hand)
    #文字首行留空，防止带表情复制不完全
    setText(text)
    time.sleep(1)
    ctrlV()
    time.sleep(1)
    altS() """





from ctypes import windll
import win32con

__PostMessageW = windll.user32.PostMessageW
def sendText(hand,msg: str):
    """
    @Description : 打字
    ---------
    @Args : msg:目标字符
    -------
    @Returns : None
    -------
    """
    for i in msg:
        __PostMessageW(hand, win32con.WM_CHAR, ord(i), 0)

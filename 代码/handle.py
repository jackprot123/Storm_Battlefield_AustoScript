import sys
import cv2
import window
from ctypes import windll, byref, c_ubyte
from pywinauto import application, timings


def get_handle(name):
    if not windll.shell32.IsUserAnAdmin():
        # 不是管理员就提权
        windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1)

    hand = windll.user32.FindWindowW(None, name)
    print('hand:',hand)
    app = application.Application(backend='uia').connect(handle=hand,visible_only=False,top_level_only=False)
    dlg = app.top_window()
    ctrl = dlg.child_window()
    try:
        handlee=ctrl.handle
        print('handle:', handlee)
        window.resize_window(hand, 1920, 1080)
        window.move_window(hand, 0, 0)
        return handlee
    except:
        print('不要放在前台1')
        sys.exit()
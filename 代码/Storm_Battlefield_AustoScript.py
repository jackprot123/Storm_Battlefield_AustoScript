#模块库
from ctypes import windll, byref, c_ubyte
from ctypes.wintypes import RECT, HWND
import time
#自定义函数
import handle
import window
import keyboard
import mouse
import match
import msg
import base

if __name__ == "__main__":
    
    # 获取句柄并调整窗口大小和位置
    hand=handle.get_handle('英魂之刃')
    window.unlock_window(hand)
    time.sleep(5)

while True:
        #进入游戏
        time.sleep(1)
        point=match.match_img(hand,'.\image\yingxiongjuexing.png')
        if point is not None:
            mouse.click_left(hand,998,681)
        else:
            print('是不是选错模式了？')
        
        Enter=False
        while Enter is not True:
            Enter,x,y=match.match_color(hand,[245, 245, 245],5,696,274,1330,670)
            if Enter is True:
                print('找到力',x,y)


        #选择英雄
        time.sleep(0.5)
        mouse.click_left(hand,1402,745)
        time.sleep(0.5)
        msg.sendText(hand,"火舞")
        time.sleep(0.5)
        mouse.click_left(hand,452,812)
        time.sleep(0.5)
        mouse.click_left(hand,1241,1051)

        
        #游戏内
        Camp_L=False
        Camp_R=False
        while not (Camp_L or Camp_R):
            Camp_L,_,_=match.match_color(hand, [16, 173, 200], 5,1668,1003,1706,1038)
            Camp_R,_,_=match.match_color(hand, [239, 32, 16], 5,1668,1003,1706,1038)
            time.sleep(0.5)
            
        
        #按P打开商店
        keyboard.key_down_up(hand,'P')
        time.sleep(1)
        #点击转换法杖
        mouse.click_left(hand,966,275)
        time.sleep(0.5)
        Game=False
        #如果在左下阵营
        if Camp_L == True:
            while (Game == False):
                print('在左下')
                #买装备
                base.Equip(hand)
                time.sleep(2)
                #泉水操作
                x1,y1,x2,y2=1652,1055,1660,1062
                Game=base.pool(hand,x1,y1,x2,y2)
        #如果再右上阵营
        elif Camp_R == True:
            while (Game == False):
                print('在右上')
                #买装备
                base.Equip(hand)
                time.sleep(2)
                #泉水操作
                x1,y1,x2,y2=1894,822,1884,818
                Game=base.pool(hand,x1,y1,x2,y2)
        
        #游戏结束
        time.sleep(5)
        mouse.click_left(hand,976,803)      #点击继续游戏
        time.sleep(5)
        mouse.click_left(hand,1578,1044)    #点击返回大厅
        time.sleep(5)
        mouse.click_left(hand,955,768)      #防止卡住
        time.sleep(5)
        time.sleep(10)



        
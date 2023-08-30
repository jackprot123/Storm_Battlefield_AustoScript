import match
import mouse
import time
import keyboard



def Equip(hand,
Equip_xmzh=False,
Equip_jsfz=False,
Equip_gz=False,
Equip_jl=False,
Equip_zh=False):
    #初始化

    # 买装备
    if Equip_xmzh==False:
        _,Equip_xmzh=match.match_img(hand,'.\image\zhihuan.png')
    print('zhihuan')
    if Equip_xmzh==True:
        #购买邪魔指环
        mouse.click_right(hand,703,281)
        time.sleep(0.5)
        
    if Equip_jsfz==False:
        _,Equip_jsfz=match.match_img(hand,'.\image\jisufazhang.png',726,249,779,329)
    print('jisu')
    if Equip_jsfz==True:
        #购买急速法杖
        mouse.click_right(hand,750,276)
        time.sleep(0.5)

    if Equip_gz==False:
        _,Equip_gz=match.match_img(hand,'.\image\guanzi.png',781,248,832,324)
    print('guanzi')
    if Equip_gz==True:
        #购买罐子
        mouse.click_right(hand,803,280)
        time.sleep(0.5)
    
    if Equip_jl==False:
        _,Equip_jl=match.match_img(hand,'.\image\jianliao.png',838,243,885,316)
    print('jianliao')
    if Equip_jl==True:
        #购买减疗杖
        mouse.click_right(hand,864,278)
        time.sleep(0.5)

    if Equip_zh==False:
        _,Equip_zh=match.match_img(hand,'.\image\zhuanhaun.png',878,242,943,317)
    print('zhuanhuan')
    if Equip_zh==True:
        #购买转换法杖
        mouse.click_right(hand,914,285)
        time.sleep(0.5)




def pool(hand,x1=1350,y1=850,x2=1350,y2=855):
    # 泉水乱走
    mouse.click_right(hand,x1,y1)
    time.sleep(2)
    # 学技能
    keyboard.key_down(hand,'lcontrol')
    keyboard.key_down(hand,'R')
    keyboard.key_up(hand,'R')
    keyboard.key_up(hand,'lcontrol')
    time.sleep(0.5)
    # 乱走
    mouse.click_right(hand,x2,y2)
    time.sleep(0.5)
    # 开大！
    keyboard.key_down_up(hand,'R')
    #法国军礼
    mouse.click_left(hand,1696,538)
    time.sleep(1)
    #检测游戏是否结束
    _,Game=match.match_img(hand,'.\image\jixuyouxi.png')
    return Game
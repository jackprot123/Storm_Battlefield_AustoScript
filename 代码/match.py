# coding=utf-8
from ctypes import windll, byref, c_ubyte
from ctypes.wintypes import RECT, HWND
import numpy as np
from PIL import Image
import cv2

GetDC = windll.user32.GetDC
CreateCompatibleDC = windll.gdi32.CreateCompatibleDC
GetClientRect = windll.user32.GetClientRect
CreateCompatibleBitmap = windll.gdi32.CreateCompatibleBitmap
SelectObject = windll.gdi32.SelectObject
BitBlt = windll.gdi32.BitBlt
SRCCOPY = 0x00CC0020
GetBitmapBits = windll.gdi32.GetBitmapBits
DeleteObject = windll.gdi32.DeleteObject
ReleaseDC = windll.user32.ReleaseDC

# 防止UI放大导致截图不完整
windll.user32.SetProcessDPIAware()

def capture(hand: HWND):
    """窗口客户区截图

    Args:
        handle (HWND): 要截图的窗口句柄

    Returns:
        numpy.ndarray: 截图数据
    """
    # 获取窗口客户区的大小
    r = RECT()
    GetClientRect(hand, byref(r))
    width, height = r.right, r.bottom
    # 开始截图
    dc = GetDC(hand)
    cdc = CreateCompatibleDC(dc)
    bitmap = CreateCompatibleBitmap(dc, width, height)
    SelectObject(cdc, bitmap)
    BitBlt(cdc, 0, 0, width, height, dc, 0, 0, SRCCOPY)
    # 截图是BGRA排列，因此总元素个数需要乘以4
    total_bytes = width*height*4
    buffer = bytearray(total_bytes)
    byte_array = c_ubyte*total_bytes
    GetBitmapBits(bitmap, total_bytes, byte_array.from_buffer(buffer))
    DeleteObject(bitmap)
    DeleteObject(cdc)
    ReleaseDC(hand, dc)

    # 返回截图数据为numpy.ndarray
    return np.frombuffer(buffer, dtype=np.uint8).reshape(height, width, 4),width,height

def match_img(hand,path,x1=None,y1=None,x2=None,y2=None):

    #hand = handle.get_handle()
    image,width,height = capture(hand)
    if x1 is not None:
        #image = image[x1:x2, y1:y2]
        image = image[y1:y2, x1:x2]

    # 转为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
    
    # 读取图片，并保留Alpha通道
    template = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    
    # 取出Alpha通道
    #try:
    #if template.any() is not None:
    #alpha = template[:,:,3]
    template = cv2.cvtColor(template, cv2.COLOR_BGRA2GRAY)
    """ cv2.imshow('Match Template', template)
    cv2.waitKey() """
    # 模板匹配，将alpha作为mask，TM_CCORR_NORMED方法的计算结果范围为[0, 1]，越接近1越匹配
    
    result = cv2.matchTemplate(gray, template, cv2.TM_CCORR_NORMED)
    
    # 获取结果中最大值和最小值以及他们的坐标
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print('maxval',max_val)
    if max_val >0.999:
        top_left = max_loc
        h, w = template.shape[:2]
        bottom_right = top_left[0] + w, top_left[1] + h
        # 在窗口截图中匹配位置画红色方框
        """ cv2.rectangle(image, top_left, bottom_right, (0,0,255), 2)
        cv2.imshow('Match Template', image)
        cv2.waitKey() """
        centerpoint=(top_left[0]+int(w/2),top_left[1]+int(h/2))
        BOOL=True
        return centerpoint,BOOL
    else:
        print('没找到')
        BOOL=False
        return None,BOOL
     


""" def match_color(img, color, tolerance=5):
    
    #img_arr = img[:, :, ::-1]
    img_arr=img
    print('img_arr',img_arr)
    
    r, g, b = color
    color_arr = np.array([r, g, b])
    print('color_arr',color_arr,np.abs(img_arr - color_arr))
    differ=np.abs(img_arr - color_arr)
    mask=np.all(differ <= tolerance, axis=-1)
    print(mask)
    if np.any(mask):
        y,x=np.where(mask)
        return True,x[0],y[0]
    else:
        return False,None,None


img=cv2.imread('.\image\shenxiang.png')
img.astype(np.ndarray)
match_color(img,[100,100,100],50)
print(type(img))
 """





def match_color(hand, color, tolerance=5,x1=None,y1=None,x2=None,y2=None):
    img,width,height=capture(hand)
  
    img.astype(np.ndarray)
    """ cv2.rectangle(img, [x1, y1], [x2,y2], (0,0,255), 2)
    cv2.imshow('Match Template', img)
    cv2.waitKey() """
    img=cv2.cvtColor(img,cv2.COLOR_RGBA2RGB)
    
    """ cv2.rectangle(img, [x1, y1], [x2, y2], (0,0,255), 2)
    cv2.imshow('Match Template', img)
    cv2.waitKey()  """

    #img=np.array('i',img)
    #img=np.array(img)
    #print('img',img)
    if x1 is not None:
        img = img[y1:y2, x1:x2] 
    img_arr=img
    
    img_arr = img[:, :, ::-1]

    #print('img_arr',img_arr)
    r, g, b= color
    color_arr = np.array([r, g, b])
    #print('color_arr',color_arr,np.abs(img_arr - color_arr))
    differ=np.abs(img_arr - color_arr)
    #print('differ=',differ)
    mask=np.all(differ <= tolerance, axis=-1)
    #print(mask)
    if np.any(mask):
        y,x=np.where(mask)
        
        if x1 is not None:
            x=int(sum(x)/len(x)+x1+5)
            y=int(sum(y)/len(y)+y1+5)
            return True,x,y
        else:
            x=int(sum(x)/len(x)+5)
            y=int(sum(y)/len(y)+5)
            return True,x,y
    else:
        return False,None,None
 





""" def match_img(hand,path,x1=None,y1=None,x2=None,y2=None):
        
    # 读取两张图片
    img1,width,height = capture(hand)
    if x1 is not None:
        image = image[x1:x2, y1:y2]
        #image = image[y1:y2, x1:x2]
    img2 = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    
    # 获取两张图片的特征
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # 匹配两张图片的特征
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    # 绘制匹配的特征点
    img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # 显示匹配的图片
    cv2.imshow('匹配的图片', img3)
    cv2.waitKey()
    cv2.destroyAllWindows()

    # 计算两张图片的相似度
    similarity = len(matches) / len(kp1)

    # 打印相似度
    print('相似度：', similarity)

    # 判断两张图片是否相似
    if similarity > 0.5:
        print('两张图片相似')
    else:
        print('两张图片不相似') """
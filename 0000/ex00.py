#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
'''

from PIL import Image,ImageFilter,ImageDraw,ImageFont
   
MARGIN = 32
# 打开一个jpg图像文件
img = Image.open('touxiang.jpg')
width,height = img.size
print(img.size)
#设置所使用的字体
font = ImageFont.truetype("C:\\WINDOWS\\Fonts\\Arial.TTF", 36)
    
#画图
draw = ImageDraw.Draw(img)
draw.text((width-MARGIN, 0), "9", (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
draw = ImageDraw.Draw(img)                          #Just draw it!
			
#另存图片
img.save("touxiang_output.jpg")

'''
'''

'''测试'''
pass

'''
gaga
haha
lala
'''
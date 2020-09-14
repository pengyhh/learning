#!/usr/bin/python
#-- coding:utf8 --   #解决中文乱码问题

f=float(input('请输入华式摄氏度：'))  #输入华式摄氏度并赋值给变量f
c=(f-32)/1.8  #计算摄氏温度
print('%.2f华式度=%.2f摄氏度' % (f,c)) #输出转换后的温度

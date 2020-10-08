#!/usr/bin/python3
print("=====================行与缩进========================")
if False:
    print("True")
else:
    print("false")
    print("a")


print("=====================多行语句========================")
total = 1 +\
        2 +\
        3
print(total)

print("=======================[], {}, 或 () 中的多行语句，不需要使用反斜杠(\)======================")
total = ['one','two','three']
print(total)

print("=====================字符串========================")
str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')
#这里的r指的是row,即row string
print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

print("=====================等待用户输入========================")
#input("\n\n按下 enter 健后退出")

print("=====================同一行显示多条语句========================")
import sys;x = 'runoob';sys.stdout.write(x+'\n')

print("=====================多个语句构成代码组========================")
if 1==2 :
   print(1)
elif 1==1 :
   print(2)
else :
   print(3)

print("=====================print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：========================")
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end="          ")
print(y, end="")
print()

print("=====================import与from...import========================")
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

from sys import argv, path  # 导入特定的成员

print('\n\n================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
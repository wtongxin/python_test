##练习：1.在控制台输入1~7；2.随机的数字每个数字对应星期几；3.如果输入的不是1~7，提示输入错误
#方法一：
# num=int(input('输入1~7随意一个数字：'))
# dic={1:'星期一',2:'星期二',3:'星期三',4:'星期四',5:'星期五',6:'星期六',7:'星期日'}
#
# if num<1 and num>7:
#     print('输入错误')
# else:
#     print('今天是{}'.format(dic[num]))
#
#方法二：
# num1=int(input('输入1~7随意一个数字：'))
# dic=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
#
# if num1<1 and num1>7:
#     print('输入错误')
# else:
#     week=num1-1
#     print('今天是'+dic[week])



##练习：四个数字：1、2、3、4，能组成多少个互不相同且无重复的三位数？各是多少？
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if (a!=b) and (a!=c) and (b!=c):
#                 print(a,b,c)



##练习：打印九九乘法表
#方法一：
# for num1 in range(1,10):
#     for num2 in range(1,num1+1):
#         print(num1,'*',num2,'=',num1*num2,end='\t')
#     print('')
#
#方法二：
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()
#
#方法三：
# for x in range(1,10):
#     for y in range(1,x+1):
#         d = x * y
#         print('%d*%d=%-2d'%(x,y,d),end = ' ' )
#     print()



##练习：字符串"axbyczdj"，如何得到结果"abcd"（切片字符串）
#方法一：
# a='axbyczdj'
# print(a[::2])
#
#方法二：
# a='axbyczdj'
# c=[]
# for i in range(len(a)):
#     if i%2==0:
#         c.append(a[i])
# print(''.join(c))



##练习：已知一个字符串为"hello_world_yoyo"，如何得到一个队列["hello","world","yoyo"]
# a='hello_world_yoyo'
# b=a.split('_')
# print(b)



##练习：统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
#方法一：
# a=[1,3,5,7,0,-1,-9,-4,-5,8]
# b=[i for i in a if i>0]
# print('大于0的个数：%s' % len(b))
# c=[i for i in a if i<0]
# print('小于0的个数：%s' % len(c))
#
# 方法二：
# num=[1,3,5,7,0,-1,-9,-4,-5,8]
# num1=0
# num2=0
# for i in num:
#     if i>0:
#         num1+=1
#     elif i<0:
#         num2+=1
#     else:
#         pass
# print('大于0的个数：',num1)
# print('小于0的个数：%s' % num2)
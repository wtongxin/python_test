#while循环
#当满足一定条件的时候才循环，具体多少循环次数没有具体规定或者规划
#语法：while (循环条件）：    （循环条件不是一成不变的，条件会变）
#         循环体


# #练习：银行利息
# #10000本金，每年利息收入7%。多少年后本兮会超过13000？
# #分析思路：
# #循环问题，没有明确的循环次数。循环条件确定：本金不超过13000。while循环
# #让我们求年限，我们用一个变量来存储答案并初始化
# year=0
# money=10000
# while money<=13000:
#     # money=money*1.07
#     # year=year+1
#     money*=1.07
#     year+=1
# # print('Year is',year)
# print('Year is %d' % year)


# #练习：累加求和
# #1-50累加求和
# #while循环必须用
# #分析思路：
# #1.用计数来表示数字，从1开始，每次增长1，只要小于51，就把数字和总和相加
# #2.循环条件：n小于51
# #3.每次n都要增加1
# #4.每次n都要跟总和相加
# #存放总和
# sum=0
# #计数器
# n=1
# while n<51:
#     sum += n
#     n+=1
# print('总和为：%d'%sum)
#
# #for循环方法：
# sum=0
# for x in range(1,51):
#     sum=sum+x
# print(sum)
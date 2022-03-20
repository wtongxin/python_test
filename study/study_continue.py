#continue语句    继续下一轮循环
#使用环境：当我们已经确定不需要继续本轮循环的时候使用


# #练习：1-100累加求和，只有当数字为奇数的时候才累加
# #分析思路：
# #1.累加求和==>for循环
# #2.奇数==>n % 2 !=0       !=:不等于,"n % 2 !=0"意思为：n除以2取余不为0
# #3.奇数就累加，偶数就进行下一轮循环
# sum=0
# for num in range(1,100):
#     if num % 2 ==0:
#         #continue继续的含义是，继续下一轮循环
#         continue
#     sum+=num
# print(sum)


# #练习：乘法表中所有乘积小于12的数字打印出来
# import sys
# #负责每一行
# for i in range(1,10):
#     #负责每一列
#     for j in range(1,10):
#         if i*j>12:
#             continue
#         #整数转字符串直接用str()就可以
#         sys.stdout.write(str(i * j))
#         sys.stdout.write(' ')
#     print(' ')






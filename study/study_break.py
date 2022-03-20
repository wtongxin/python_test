#break语句
#英文愿意就是中断的意思，在python中，保持了英文
#作用：无条件终止循环并跳出循环体


# #练习：在50-100之间查找第一个可以被9整除的数
# #分析思路：
# #1.范围给出来了，范围明确，增长规律
# #2.对于此类业务，优先选用for循环
# #3.要求找到第一个==>找到第一个就应该退出
# #4.退出==>break
# for num in range(50,101):
#     #被9整除如何表示？
#     #如果用9取余等于0，则表示能被整除
#     if num%9==0:
#         print(num)
#         break


# #对于嵌套多重循环，break语句值退出跟它最近的一次循环
# #练习：输出9*9乘法表
# #如果想成的积大于81，则不需要显示
# #乘法表是一个典型双重for循环结构
# #如果乘积大于81，我们结束本轮循环
# #结束用break
# #注意：不能使用print语句，因为print语句默认输出后会换行
# #在sys模块中有write函数可以使用。write函数写出来默认不换行
# #导入sys
# # noinspection PyUnresolvedReferences
# import sys
# #负责乘法表行数的循环
# for x in range(1,10):
#     #负责乘法表列数的循环
#     for y in range(1,10):
#         if x*y>81:
#             break
#         sys.stdout.write(str(x*y))
#         sys.stdout.write(' ')
#     print(' ')


# #打印一个9*9乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,'*',j,'=',i*j,end='\t')
#     print('')
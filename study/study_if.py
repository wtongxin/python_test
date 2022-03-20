# #if语句案例：
# #老师对大家的考试成绩进行评定，采用ABCDE五级进行评定，A是最好成绩。
# #如果90分（包含此分数）以上，则输出A
# #如果80分（包含此分数）以上，则输出B
# #如果70分（包含此分数）以上，则输出C
# #如果60分（包含此分数）以上，则输出D
# #其余，则输出E
# score=int(input('请输入一个分数：'))
# if score>=90:
#     print('A')
# elif score>=80 and score<90:
#     print('B')
# elif score>=70 and score<80:
#     print('C')
# elif score>=60 and score<70:
#     print('D')
# else:
#     print('E')


# #判断一个学生成绩，如果大于60分，则学生成绩及格，否则，重考
# score=int(input('请输入您的成绩：'))
# if score>=60:
#     print('您已经及格！')
# else:
#     print('对不起，您需要重考！')


# #输入学生成绩，大于等于90分，则输出A，否则，判断是否大于60，如果大于等于60，则输出及格，否则，输出不及格
# score=int(input('请输入您的成绩：'))
# if score>=90:
#     print('A')
#     print('You are the best!')
#     print('Thank you!')
# else:
#     if score>=60:
#         print('成绩及格')
#     else:
#         print('成绩不及格')
#
# score=int(input('请输入您的成绩：'))
# if score>=90:
#     print('A')
#     print('You are the best!')
#     print('Thank you!')
# elif score>=60:
#     print('成绩及格')
# else:
#     print('成绩不及格')


# #演示else配对问题,else用于跟与它平级的if配对
# score=87
# if score>90:
#     if score>95:
#         print('You are the best!')
# else:
#     print('一般般啦')


# #练习：if语句或者if…else语句
# #模拟上海出租车收费系统：
# #1.3公里以内，收取基本起步费用13元
# #2.超出3公里，则每公里加2.3元（2.3元/km）
# #3.空驶费，超出15公里，每公里加收单价的50%空驶费用，即3.45元/km
# #要求：输入驾驶里程计算费用
# #分析思路：
# #1.要求用户输入总里程
# #2.判断用户里程，如果小于3km，则输出13元
# #3.如果大于3km并且小于15km，则收取 13+（里程数-3）*2.3 元
# #4.如果大于15公里，则收取 13+12*2.3+（里程数-15）*3.45 元
# #5.输出费用
# km=float(input('请输入行驶里程数：'))   #float表示浮点数，即小数，里程很可能包含小数
# cost=0
# if km<=3:
#     cost=13
#     print('收取',cost,'元')
# else:
#     if km<=15:
#         cost=13+(km-3)*2.3
#         print('收取',cost,'元')
#     else:
#         cost=13+(15-3)*2.3+(km-15)*3.45
#         print('收取',cost,'元')


# #三元操作符（元：操作数的意思，所谓三元，就是一个操作符带动三个操作数一起运算）
# #语法：x if 条件 else y（假如条件成立，返回x，否则，返回y）
# #表示：如果if条件判断为真，则返回值x，否则返回值y
# #三元运算符示例
# a=34 if 3<5 else 1    #如果3<5成立（为True），返回34，否则，返回1。所以返回的是34
# print(a)
# a=34 if 3>5 else 1    #如果3<5成立（为True），返回34，否则，返回1。所以返回的是1
# print(a)


# #练习：三元运算符
# #1.a,b两数由用户输入
# #2.比较大小，把最大值存入变量c
# #分析思路：
# #1.用户输入可以用input函数，然后用int转换
# #2.比较两数，把大值存入c
# a=int(input('请输入数字A：'))
# b=int(input('请输入数字B：'))
# c= a if a>b else b
# print(c)


# #练习：利用三元运算符求最大值
# #要求：
# #1.a,b,c由用户输入三个
# #2.比较大小，最大值输出
# #分析思路：先求两个数间的最大值，再用这个最大值和后边的数相比较
# a=int(input('请输入A:'))
# b=int(input('请输入B:'))
# c=int(input('请输入C:'))
# #求a,b最大值代码为a if a>b else b
# #此处，只要把c当成b，则a代表原来a,b最大值即可。d=a if a>c else c
# d=(a if a>b else b) if (a if a>b else b)>c else c
# print(d)













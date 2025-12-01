
# age = 10
#
# if age >= 18:
#     print("你已经成年了")
# else:
#     print("小朋友你好！！！")
#
# score = 50
# if score >= 90:
#     print("成绩优秀")
# elif score >= 80:
#     print("成绩良好")
# elif score >= 70:
#     print("成绩中等")
# elif score >= 60:
#     print("成绩及格")
# else:
#     print("成绩不及格")

weight = 80
if weight>=180:
    print("你超重了，要手术抽脂")
elif weight>=150:
    print("你该运动减肥了")
elif weight>=120:
    print("继续保持，体重正常")
elif weight>=60:
    print("要增肥了")
else:
    print("你太瘦了，要看医生")

# if 与 运算符 and   -> java 的 &&
age=10
if_has_license = True

if age>=18 and if_has_license:
    print("you can drive car")
else:
    print("you cannot drive car")

# if 与 运算符 or  -> Java 的  || 运算符, 以及判断 ==
# day = "Saturday"
day = "Monday"
if day=="Saturday" or day=="Sunday":
    print("周末愉快！！！！")
else:
    print("工作日，好好干活呀，年轻人")

# 列表长度判断
numbers = [1, 2, 3, 4, 5]
if len(numbers) > 3:
    print("列表元素较多")
elif len(numbers) > 0:
    print("列表有少量元素")
else:
    print("列表为空")

num_element = 6
if num_element in numbers:
    print("是的")
else:
    print("找不着元素",num_element)


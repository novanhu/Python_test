# 三元运算符
# 条件 ? 值1 : 值2                                java (a > b) ? a : b
# 值1 if 条件 else 值2                            python  a if a > b else b
score = 85
result = "及格"if score>=60 else "不及格"
print(result)

#Python 中的嵌套
score = 85
grade = "优秀" if score >= 90 else "良好" if score >= 70 else "及格" if score >= 60 else "不及格"
print(grade)


# Python - 多行写法更易读
grade = (
    "优秀" if score >= 90 else
    "良好" if score >= 70 else
    "及格" if score >= 60 else
    "不及格"
)
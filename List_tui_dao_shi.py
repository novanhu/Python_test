squares = [i * i for i in range(10)]

# 2. 过滤出大于50的数字
numbers = [30, 55, 20, 80, 45, 90]
large_numbers = [num for num in numbers if num > 50]
for item in large_numbers:
    print(item)

# 3. 将数字转换为描述
values = [10, -5, 0, 25]
descriptions = ["正数" if value > 0 else "负数" if value < 0 else "零" for value in values]
for element in descriptions:
    print(element)
print(descriptions)

descriptions2 = ["正数" if value > 0 else "负数" if value < 0 else "零" for value in values]
# 记住这个模式：[你想要什么 for 循环变量 in 数据源 if 条件]

# 模式1：过滤模式
# [表达式 for 元素 in 可迭代对象 if 条件],      ↑ 先循环，再条件判断（过滤）,if 在最后 → 过滤（元素可能变少）
# [x for x in list if condition]
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)

# 模式2：条件表达式模式
# [值1 if 条件 else 值2 for 元素 in 可迭代对象]   对所有元素进行条件判断（转换）, if-else 在最前 → 转换（元素数量不变）
# [value1 if condition else value2 for x in list]
numbers = [1, 2, 3, 4, 5, 6]
labels = ["偶数" if x % 2 == 0 else "奇数" for x in numbers]
print(labels)

# [转换逻辑 for x in list if 过滤条件]
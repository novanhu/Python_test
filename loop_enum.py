"""
Python 枚举遍历（带索引的遍历）
枚举遍历相当于 Java 中的 for (int i=0; i<list.size(); i++)，可以同时获取索引和元素。
"""
# 枚举遍历相当于 Java 中的 for (int i=0; i<list.size(); i++)，可以同时获取索引和元素。
# 基本用法：enumerate()

fruits = ["榴莲","菠萝蜜","芒果","释迦果","杨桃","奇异果"]
for index, fruit in enumerate(fruits):
    print(f" index {index}, {fruit}")

# start 是索引起始值
for index, fruit in enumerate(fruits, start=100):
    print(f" index {index}: {fruit}")

# 画重点，index 是重点元素

# {键: 值 for 循环变量 in 可迭代对象}
fruit_dict  = {index: fruit for index, fruit in enumerate(fruits)}
fruit_dict2 = {fruit: index for index, fruit in enumerate(fruits)}
print(fruit_dict)
print(fruit_dict2)

numbers = [1, 2, 3, 4, 5]
square_dict = {x: x**2 for x in numbers}
print(square_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
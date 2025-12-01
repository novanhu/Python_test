# test method
def add(a,b):
    return a+b

result = add(3,5)
print(result)
print(add(8,10))

def greet(name, message):
    # return f"{name}, {message}"
    print(f"{name}, {message}")

greet("Eric", "好久不见呀！")

# 默认参数
def defaultGreet(name,message="hello !"):
    return f"{name}, {message}"

print(defaultGreet("Alic"))
print(defaultGreet("Alice","我太想你了！"))

# 可变参数
# 接受任意数量的关键字参数：定义函数时使用 **kwargs，可以使函数能够接受任意数量的关键字参数，而无需事先指定参数名。
# Note: 将参数转换为字典：在函数内部，kwargs 会被当作一个字典来处理，其中键是参数名，值是参数值。
# 灵活处理函数参数：方便在不确定函数将接收多少个关键字参数时编写函数。
def kwargsGreet_print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
kwargsGreet_print_info(name="Alice",age=15,city="Beijing" )

# 返回值，可以是None, 可以是多个返回值,
# Note: 不解包返回,多个返回值，实际返回的是元组
# Note: 也可以解包返回的
def calculate(a,b):
    sum_result = a + b
    product = a * b
    return  sum_result, product
result = calculate(3,7)
print(result)
# 下面就是解包的返回值
sum_result, product = calculate(3,7)
print(sum_result)
print(product)

# Python 的一等公民是函数，可以作为变量进行值传递
def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def calculate_2(operation,a,b):
    return operation(a,b)

print(calculate_2(add,1,2))
print(calculate_2(multiply,1,2))

# python 也有 Lambda 函数， 跟java 的  Lambda表达式一样
# Python lambda ：
# 基础语法   ---  lambda 参数: 表达式
add = lambda a, b: a + b
print(add(5, 3))  # 8

# 在排序中使用
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
students.sort(key=lambda student: student[1])  # 按年龄排序
print(students)  # [('Bob', 20), ('Charlie', 23), ('Alice', 25)]

# key 参数的作用
# key 参数接受一个函数，这个函数会应用到列表中的每个元素上，然后根据函数的返回值进行排序。


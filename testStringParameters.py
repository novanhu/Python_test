
# Python (动态类型) vs Java/TypeScript (静态类型)
# Python - 无需声明类型
#1. 变量与数据类型对比
name = "John"          # str
age = 25              # int
height = 1.75         # float
is_student = True     # bool

# 对应 TypeScript
# let name: string = "John";
# let age: number = 25;
# let isStudent: boolean = true;

#print() 中用逗号分隔各个参数即可
print("Hello, World!")
print(name,age,height,is_student)

#列表， 字典
fruits = ["苹果", "香蕉", "橙子", 1, True, False]
scores = {"数学": 95, "英语": 88, "及格": True, "法治": "不通"}

print("水果列表:", fruits, "成绩单:", scores)


print("Hello", end=" ******")      # 以空格结束，不换行
print("World", end="!")      # 以!结束，不换行
print("Next line")
# 输出：Hello World!Next line


# 个人信息打印
name = "张三"
age = 20
city = "北京"
hobbies = ["读书", "游泳", "编程"]

print("个人信息:")
print("姓名:", name, "年龄:", age, "城市:", city)
print("爱好:", hobbies)

# 或者用自定义格式
print(name, age, city, sep=" | ", end=" --- 个人信息\n")

# f-string
print(f"张三信息{hobbies}dddddddd")

# 多行string 的写法
message=(
    f"hahahah\n"
    f"xixixixi\n"
    f"lalalala\n"
    f"luululu\n"
)
print(message)

contentOfInput = input("Please enter you content info here: + \n")
print(contentOfInput)

data = input()
print("你输入的是：" + data)
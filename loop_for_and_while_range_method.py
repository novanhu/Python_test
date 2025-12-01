fruits = ["苹果", "香蕉", "橙子"]

print("*******loop----for********")

# 遍历列表元素
for fruit in fruits:
    if fruit=="橙子":
        print(fruit,"真酸")
    else:
        print(fruit,"真甜")

for char in "Hello python world":
    print(char,"")

print("***************")

for i in range(7):
    print(i)

print("***************")

for i in range(1,7):
    print(i)

print("***************")
for i in range(1,7,2):
    print(i)


print("*******loop----while********")
count = 0
while count < 10:
    print(f"计数: {count}")
    print("计数dadada ,",count)
    count += 1

# 循环控制语句 break, continue, if-else
hehe = 6
while hehe < 10:
    if hehe==5:
        continue;
    print(f"计数: {hehe}")
    print("计数hehehe ,",hehe)
    hehe += 1


for i in range(5):
    if i == 2:
        continue
    print(i)

#4. 实用技巧, 遍历 带索引， 遍历字典， 嵌套循环
fruits_array = ["苹果", "香蕉", "橙子"]
for i in fruits_array:
    print(i)
for i in range(len(fruits_array)):
    print(f"{i},{fruits_array[i]}")

for index, fruithaha in enumerate(fruits_array):
    print(f"hahaha: {index}: {fruithaha}")



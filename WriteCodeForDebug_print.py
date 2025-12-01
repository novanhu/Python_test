print("hahahhaha")

name = "novan hu"
age = 18
height = 162.2
weight111 = int(input())
is_true = False

# print 里面加f, 就可以在双引号里面添加花括号，且花括号里面可以加变量
message = (
    f"name:{name}"
    f"age: {age}"
    f"height:{height}"
    f"is that ture: {is_true}"
    f"weight: {weight111}"

)

basicInfo = input("input basic message here: " + message)
print(message)

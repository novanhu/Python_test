#python if/else

def hello():
    print("hello")
    print("world")

def calculate_sum(a,b):
    if(a+b)>18:
        return a+b
    else:
        return "to yong too simple."

print(hello())
print(calculate_sum(10,9))
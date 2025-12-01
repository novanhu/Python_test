score = 85
user = None

# 三元表达式
print(f"Grade: {'Pass' if score >= 60 else 'Fail'}")  # Grade: Pass

# 处理 None
print(f"User: {user if user else 'Guest'}")           # User: Guest
print(f"User: {user or 'Guest'}")                     # User: Guest

# 复杂条件
temperature = 22
print(f"Water is {'solid' if temperature <= 0 else 'gas' if temperature >= 100 else 'liquid'}")
# Water is liquid
"""
9. 字典的特点
特性	说明
无序性	Python 3.7+ 保持插入顺序
键唯一性	键必须唯一，重复键会覆盖
键的类型	键必须是不可变类型（字符串、数字、元组）
动态大小	可以随时添加、删除键值对
高性能	基于哈希表，查找速度很快 O(1)
总结
关键记住：

Python 字典 ≈ Java HashMap
使用 {} 创建，dict[key] 访问
get() 方法安全访问，避免 KeyError
items() 遍历键值对，keys() 遍历键，values() 遍历值
字典推导式让创建字典更简洁
支持嵌套，适合复杂数据结构
"""

scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# 遍历键
for key in scores:
    print(key)

for key in scores.keys():
    print(key)

# 遍历值
for value in scores.values():
    print(value)

# 遍历键值对
for key, value in scores.items():
    print(f"{key}: {value}")
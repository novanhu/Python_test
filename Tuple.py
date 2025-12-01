# Python 元组 - 使用圆括号

# 不可变性	创建后不能修改
# 有序性	    保持元素顺序
# 异构性	    可以包含不同类型
# 可哈希	    如果元素都可哈希，元组可哈希
# 性能好	    比列表更轻量

# 元组是不可变的列表
# 使用 () 创建，单元素需要加逗号
# 支持解包操作，非常方便
# 可以作为字典键
# 性能比列表更好
# 适合存储不应该修改的数据
# 元组是 Python 中保证数据完整性和提高性能的重要工具！

colors = ("red", "green", "blue")
numbers = (1, 2, 3, 4, 5)

# 混合类型
mixed = (1, "hello", 3.14, True)

# 创建空元组
empty_tuple = ()
empty_tuple2 = tuple()

# 单个元素的元组（注意逗号）
single_element = (42,)        # 这是元组
not_a_tuple = (42)            # 这是整数，不是元组！

print(type(single_element))   # <class 'tuple'>
print(type(not_a_tuple))      # <class 'int'>
print(not_a_tuple)      # <class 'int'>
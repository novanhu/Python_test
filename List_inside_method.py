"""
访问元素
访问	 list[index]
长度	len(list)
最后一个	list[-1]

添加元素
list.append(element)
list.insert(index, element)
list.extend(anotherList)

删除元素
操作	        Java ArrayList	                 Python List
按索引删除	list.remove(index)	             del list[index] 或 list.pop(index)
按值删除	    list.remove(element)	         list.remove(element)
弹出末尾	    list.remove(list.size()-1)	     list.pop() 删最后一个元素

list.clear()列表清空

切片操作

排序和反转
sort 默认是升序，sort(reverse=true)降序， reverse 就是降序

"""
numbers = [10, 20, 30, 40, 50]
print(numbers[0])      # 10
print(len(numbers))    # 5
print(numbers[-1])     # 50 (最后一个)
print(numbers[-2])

numbers = [1, 2, 3, 4, 5]
numbers[0] = 100           # 修改元素
numbers.append(6)          # 添加元素 → [100, 2, 3, 4, 5, 6]
numbers.insert(1, 200)     # 插入元素 → [100, 200, 2, 3, 4, 5, 6]

print(numbers)
del numbers[0]
print(numbers)
numbers.remove(2)
print(numbers)
numbers.pop()
print(numbers)
numbers.clear()
print(numbers)

# 切片操作
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])     # [2, 3, 4]      (索引2到5，不包括5)
print(numbers[:3])      # [0, 1, 2]      (开始到索引3)
print(numbers[7:])      # [7, 8, 9]      (索引7到结束)
print(numbers[::2])     # [0, 2, 4, 6, 8] (步长为2)
print(numbers[::-1])    # [9, 8, 7, ...] (反转列表)


numbers = [3, 1, 4, 1, 5]
numbers.sort()                  # 升序排序 [1, 1, 3, 4, 5]
numbers.sort(reverse=True)      # 降序排序 [5, 4, 3, 1, 1]
numbers.reverse()               # 反转 [1, 1, 3, 4, 5] → [5, 4, 3, 1, 1]

sorted_numbers = sorted(numbers)            # 升序
sorted_desc = sorted(numbers, reverse=True) # 降序
print(sorted_numbers)
print(sorted_desc)
print(sorted_desc.reverse())


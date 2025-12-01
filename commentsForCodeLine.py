"""
三引号就是多行注释， 作为块注释

文档字符串是模块、函数、类或方法定义中的第一个语句，用于描述其用途。
"""
# #号是单行注释


def test_docstring_positions():
    """这是正确的文档字符串 - 会被识别"""
    x = 5
    """这不会被识别为文档字符串"""
    return x

print("test_docstring_positions 的文档字符串:")
print(test_docstring_positions.__doc__)


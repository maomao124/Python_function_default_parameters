"""
 * Project name(项目名称)：Python函数默认参数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/25 
 * Time(创建时间)： 20:07
 * Version(版本): 1.0
 * Description(描述)：
 在调用函数时如果不指定某个参数，Python 解释器会抛出异常。为了解决这个问题，Python 允许为参数设置默认值，
 即在定义函数时，直接给形式参数指定一个默认值。这样的话，即便调用函数时没有给拥有默认值的形参传递参数，该参数可以直接使用定义函数时设置的默认值。
def 函数名(...，形参名，形参名=默认值)：
    代码块
注意，在使用此格式定义函数时，指定有默认值的形式参数必须在所有没默认值参数的最后，否则会产生语法错误。
 """


def f1(a, b):
    """
    没有默认参数
    :param a:
    :param b:
    :return:
    """
    return a + b


def f2(a=0, b=0):
    """
    有默认参数
    :param a:
    :param b:
    :return:
    """
    return a + b


def f3(a, b=0):
    """
    1到2个参数
    :param a:
    :param b:
    :return:
    """
    return a + b


# def f4(a=0, b):
#     """
#     不允许
#     :param a:
#     :param b:
#     :return:
#     """
#     return a + b


if __name__ == '__main__':
    print(f1(2, 4))
    # 异常
    # print(f1(5))

    print(f2(6, 7))
    print(f2(6))
    print(f2())

    print(f3(6, 7))
    print(f3(6))
    # 异常
    # print(f3())

    # 查看函数的默认值参数的当前值，其返回值是一个元组
    print(f2.__defaults__)

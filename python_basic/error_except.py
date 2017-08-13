# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/9 20:07'

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except (RuntimeError, TypeError, NameError, ValueError):
#         print("Oops!  That was no valid number.  Try again")





# import sys
#
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise


# def this_fails():
#     x = 1/0
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)

# import sys
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except IOError:
#         print('cannot open', arg)
#     else:  # 当没有任何异常发生时，执行
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()
#

"""
raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
"""
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise


"""用户自定义异常"""
# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return repr(self.value)
#
# try:
#     raise MyError(2*2)
# except MyError as e:
#     print('My exception occurred, value:', e.value)



# class Error(Exception):
#     """Base class for exceptions in this module."""
#     pass
#
# class InputError(Error):
#     """Exception raised for errors in the input.
#
#     Attributes:
#         expression -- input expression in which the error occurred
#         message -- explanation of the error
#     """
#
#     def __init__(self, expression, message):
#         self.expression = expression
#         self.message = message
#
# class TransitionError(Error):
#     """Raised when an operation attempts a state transition that's not
#     allowed.
#
#     Attributes:
#         previous -- state at beginning of transition
#         next -- attempted new state
#         message -- explanation of why the specific transition is not allowed
#     """
#
#     def __init__(self, previous, next, message):
#         self.previous = previous
#         self.next = next
#         self.message = message


"""如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，
而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后再次被抛出"""
def divide(x, y):
    try:
        # result = x // y  # 对商取整
        result = x /y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(1,0)
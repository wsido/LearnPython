#这是一个注释
print("Hello world")

#Hello world

'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号
这是多行注释，用三个单引号
'''
print("Hello China")
#Hello China

"""
这是多行注释，用三个双引号
这是多行注释，用三个双引号
这是多行注释，用三个双引号
"""
print("Hello World")
#hello china

print("Hello Mr.l")


'''+	加	1 + 1
-	减	2 - 1
*	乘	3 * 4
/	除	3 / 4
//	整除（地板除）	3 // 4
%	取余	3 % 4
**	幂	2 ** 3
'''

print(1+1) #2
print(2-1) #1
print(3*4) #12
print(3/4) #0.75
print(3//4) #0
print(3%4) #3
print(2**3) #8



'''>	大于	2 > 1
>=	大于等于	2 >= 4
<	小于	1 < 2
<=	小于等于	5 <= 2
==	等于	3 == 4
!=	不等于	3 != 5
'''



print(2 > 1)  # True
print(2 >= 4)  # False
print(1 < 2)  # True
print(5 <= 2)  # False
print(3 == 4)  # False
print(3 != 5)  # True

'''and	与	(3 > 2) and (3 < 5)
or	或	(1 > 3) or (9 < 2)
not	非	not (2 > 1)
'''

print((3 > 2) and (3 < 5))  # True
print((1 > 3) or (9 < 2))  # False
print(not (2 > 1))  # False

'''
~	按位取反	~4
&	按位与	4 & 5
`	`	按位或
^	按位异或	4 ^ 5
<<	左移	4 << 2
>>	右移	4 >> 2
'''
print(bin(4))  # 0b100
print(bin(5))  # 0b101
print(bin(~4), ~4)  # -0b101 -5
print(bin(4 & 5), 4 & 5)  # 0b100 4
print(bin(4 | 5), 4 | 5)  # 0b101 5
print(bin(4 ^ 5), 4 ^ 5)  # 0b1 1
print(bin(4 << 2), 4 << 2)  # 0b10000 16
print(bin(4 >> 2), 4 >> 2)  # 0b1 1

x, y = 4, 5
small = x if x < y else y
print(small)  # 4

'''
操作符	名称	示例
in	存在	'A' in ['A', 'B', 'C']
not in	不存在	'h' not in ['A', 'B', 'C']
is	是	"hello" is "hello"
is not	不是	"hello" is not "hello
'''
letters = ['A', 'B', 'C']
if 'A' in letters:
    print('A' + ' exists')
if 'h' not in letters:
    print('h' + ' not exists')

# A exists
# h not exists

a = "hello"
b = "hello"
print(a is b, a == b)  # True True
print(a is not b, a != b)  # False False

a = ["hello"]
b = ["hello"]
print(a is b, a == b)  # False True
print(a is not b, a != b)  # True False
'''
注意：

is, is not 对比的是两个变量的内存地址
==, != 对比的是两个变量的值
比较的两个变量，指向的都是地址不可变的类型（str等），那么is，is not 和 ==，！= 是完全等价的。
对比的两个变量，指向的是地址可变的类型（list，dict，tuple等），则两者是有区别的。
'''
print(-3 ** 2)  # -9
print(3 ** -2)  # 0.1111111111111111
print(1 << 3 + 2 & 7)  # 0
print(-3 * 2 + 5 / -2 - 4)  # -12.5
print(3 < 4 and 4 < 5)  # True

'''
3. 变量和赋值
在使用变量之前，需要对其先赋值。
变量名可以包括字母、数字、下划线、但变量名不能以数字开头。
Python 变量名是大小写敏感的，foo != Foo。
'''
teacher = "老马的程序人生"
print(teacher)  # 老马的程序人生
myTeacher = "老马的程序人生"
yourTeacher = "小马的程序人生"
ourTeacher = myTeacher + ',' + yourTeacher
print(ourTeacher)  # 老马的程序人生,小马的程序人生
# 运行一下就好啦
set_1 = {"欢迎","学习","Python"}
print(set_1.pop())
print("整型")
a = 1031
print(a, type(a))
# 1031 <class 'int'>
a=1031
print(bin(a))
print(a.bit_length())
print("浮点型")
print(1, type(1))
# 1 <class 'int'>
print(1., type(1.))
# 1.0 <class 'float'>
a = 0.00000023
b = 2.3e-7
print(a)  # 2.3e-07
print(b)  # 2.3e-07

import decimal
from decimal import Decimal
'''
Python 里面有很多用途广泛的包 (package)，用什么你就引进 (import) 什么。包也是对象，也可以用上面提到的dir(decimal) 来看其属性和方法。

【例子】getcontext() 显示了 Decimal 对象的默认精度值是 28 位 (prec=28)。
'''
b = Decimal(1) / Decimal(3)
print(b)

# 0.3333333333333333333333333333

decimal.getcontext().prec = 4
c = Decimal(1) / Decimal(3)
print(c)

# 0.3333

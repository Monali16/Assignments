Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x, y, z = 1, 3.1, 'Moni'
>>> print(x)
1
>>> type(x)
<class 'int'>
>>> y
3.1
>>> type(y)
<class 'float'>
>>> z
'Moni'
>>> type(z)
<class 'str'>
>>> x = 1+3j
>>> y = 9
>>> x,y = y,x
>>> x
9
>>> y
(1+3j)
>>> x,y = 10, 30
>>> result = x
>>> x=y
>>> y = result
>>> x
30
>>> y
10
>>> x,y = y,x
>>> x
10
>>> y
30
>>> value = input('Enter the Value : ')
Enter the Value : 16
>>> value
'16'
>>> value = raw_input('Please enter the value : ')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    value = raw_input('Please enter the value : ')
NameError: name 'raw_input' is not defined
>>> 
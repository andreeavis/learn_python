# text #

### Conversions 


```code here```

Keyboard shortcut to comment lines in Sublime Text 3. In Sublime Text 2 it was possible to comment out a line or a block of lines with Ctrl + / and Ctrl + Shift + / . According to the menu Edit > Comment these shortcuts should be valid, but in Sublime Text 3 (build 3047) they no longer seem to work.

#FLOW CONTROL
-> comparison

>>> name-14]
  File "<stdin>", line 1
    name-14]
           ^
SyntaxError: invalid syntax
>>> name[-15]
'n'
>>> name[-16]
'A'
>>> name[-17]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> var1= 2
>>> var2 = 5
>>> var1 + var2
7
>>> var3 = '5'
>>> var1 + var3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> int('3')
3
>>> int('sss')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'sss'
>>> int(var3)
5
>>> str()
''
>>> input()
haha
'haha'
>>> print(input())
"I am super wesome"
"I am super wesome"
>>> print(input('What is your pet's name?"))
  File "<stdin>", line 1
    print(input('What is your pet's name?"))
                                  ^
SyntaxError: invalid syntax
>>> print(input('What is your pet's name?'))
  File "<stdin>", line 1
    print(input('What is your pet's name?'))
                                  ^
SyntaxError: invalid syntax
>>> print(input('What is your pet\'s name?'))
What is your pet's name?abraham
abraham
>>> print(input('What is your pet\'s name? '))
What is your pet's name? abraham
abraham
>>> print(pet)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pet' is not defined
>>> print(input('What is your pet\'s name? '))
What is your pet's name? abraham
abraham
>>> pet
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pet' is not defined
>>> pet
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'pet' is not defined
>>> 3 > 7
False
>>> 3 < 7
True
>>> 3 == 7
False
>>> 47 > 3
True
>>> 11 < 25
True
>>> 23 > 4
True
>>> 5 > 123
False
>>>   = 23
  File "<stdin>", line 1
    = 23
    ^
IndentationError: unexpected indent
>>> b = 5
>>> a = 23
>>> if a > b:
... print("You win!")
  File "<stdin>", line 2
    print("You win!")
        ^
IndentationError: expected an indented block
>>> if a > b:
... print("You win!")
  File "<stdin>", line 2
    print("You win!")
        ^
IndentationError: expected an indented block
>>> if a > b:
...     print("You win!")
... else:
...     print("you lose!")
...
You win!
>>> b = 100
>>> if a > b:
...     print('You win!')
... else:
...     print('You lose!')
...
You lose!
>>>  a== b
  File "<stdin>", line 1
    a== b
    ^
IndentationError: unexpected indent
>>> a == b
False
>>> a = b
>>> b
100
>>> a
100
>>> a == b
True
>>> 'cat' < 'dog'
True
>>> 'cat' > 'dog'
False
>>> 2 < 10
True
>>> '2' < '5'
True
>>> '2' < '10'
False
>>> 'week1' < 'week10'
True
>>> 'week01' < 'week10'
True
>>> if a == b:
...     print('they are!')
... else:
...     print('they aren\'t equal!')
...
they are!
>>>
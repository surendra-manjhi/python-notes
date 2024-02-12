# Python is known for its powerful number system or calculation as it is used for data analysis.

## Operation can be performed in numbers-

+, -, \*, /, \*\*, %

Operator Overloading - Ability of operator to perform some operation to the operands based on their types. Such as -

-   3 + 2 = 5 // num type operands leads to addition

-   "man" + "jhss" = "manjhss" // string type operands leads to concatanation

Assignment: repr(), str(), print()

## Comparison operators

> , <, ==, != // return bool value (True or False)

## math pkg

import math

math.floor(3.5) // 3 returns bottom value
math.floor(-3.5) // -4

math.trunc(2.8) // 2 returns value towards 0
math.trunc(-2.8) // -2 returns value towards 0

oct(64) // 0o100 returns octa value
hex(64) // 0x40 returns hexa value
bin(64) // 0b1000000 return binary value

int(64) // 64
int(6.4) // 6

int("64", 8) // 52 return octa(8 base value) value

int("10000", 2) // 16 return binary(2 base value) value

x = 1
x << 2 // left shift
4

## random pkg

import random

random.random() // 0.8 return value from 0 to 1

random.randint(1, 10) // 6 returns between 1 to 10(10 excluded)

random.choice([1,2,3]) // 2 returns random choice

random.shuffle([1,2,3]) // [2,1,3] returns shuffled list

## While dealing with decimal-

Use: decimal pkg

decimal.Decimal('0.2')

for fraction use fractions pkg

fraction.Fraction(2, 7)

## Sets and Boolean are also considered as number

set01 = {1,2,3} // syntax
set() // empty sets

we can perform set operations easily in python such as union and many more.

True is treated as 1
False as 0

True + 4 // returns 5

True == 1 // True

True is 1 // False as they are different obj but under the hood they contains same value

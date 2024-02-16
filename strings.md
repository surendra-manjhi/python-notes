name = ' ', " ", """ """ // different ways of initialization

String is also treated as list so that we can extract individual charactor.

name = "manjhss"
print(name[0]) // returns "m"

Slicing slices string based on given param in square brackets. One param is starting and second param is end of slice but that value is excluded (means treated as n - 1). Indecing starts from 0.

sliced = name[0:3] // "man"
sliced = name[-1] // "s"
sliced = name[0:3:2] // "mn" 2 is skipping value treated as 1 (n-1)

String supports Unicode char.

String methods

lower() 
upper()
strip() // trims unnecessary space
replace(a, b) // a is to be replace, b is replace with
split(", ") // splits string in list & param defines splitter
find("man") // returns index value. if str is not found returns -1
count("s") // returns no. of times "s" is repeated in nums

format() // formats str with variable 

name = "manjhss"
greet = "Good morning, {}" // {} is a placeholder

print(greet.format(name)) // Good morning, manjhss

"_".join([1,2,3]) // 1_2_3 (list to str)

len(str_var) // returns length

r"man\njhss" raw str

negative indexing in slicing should be start from low neg num such as [-5: -1], [-1: -5] doesn't work in this case

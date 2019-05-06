# 定义字符串变量 type_of_people
type_of_people = 10
# 定义格式化字符串变量 x
x = f"There are {type_of_people} type of people."

# 定义字符串变量 binary, do_not
binary = "binary"
do_not = "don't"
# 定义格式化字符串变量 y
y = f"Those who know {binary} and those who {do_not}."

# 输出 x, y
print(x)
print(y)
# 格式化字符串输出: f"string"
print(f"I said: {x}")
print(f"I also said: '{y}'")


# 定义字符串变量 hilarious, joke_evaluation
hilarious = "False"
joke_evaluation = "Isn't that joke so funny?! {}"

# 格式化字符串输出: .format()
print(joke_evaluation.format(hilarious))

# 定义两个字符串变量
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

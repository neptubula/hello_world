# 定义诸多变量
name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inch
weight = 180 #lbs
eyes = 'blue'
teeth = 'White'
hair = 'Brown'

# 输出格式化字符串
print(f"Let's talk about {name}")
print(f"He's {height * 2.54} centmeters tall.")
print(f"He's {weight * 0.45} kilometers heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes an {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get i texactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

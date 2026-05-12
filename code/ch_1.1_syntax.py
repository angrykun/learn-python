name = "Bob"  # 字符串
age = 25  # 数字
is_active = True
nothing = None  # NoneType

print(f"my name is {name} and i'm {age} years old.")
print("is_active =", is_active)

price = 19.99
msg = f"{name} brought for ${price:.2f}"
print(msg)

# 条件循环
age = 20

if age < 13:
    print("儿童")
elif age < 20:
    print("青少年")
else:
    print("成年人")

# for循环
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(fruit)

# range
for i in range(5):
    print(i)


# 函数
def greet(name: str) -> str:
    return f"Hello, {name}"


result = greet(name)
print(result)


# exercise
# Q1
for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)


# Q2
def fin_longest(words: list[str]) -> str:
    max_length = 0
    max_word = ""
    for word in words:
        current_length = len(word)
        if current_length > max_length:
            max_length = current_length
            max_word = word
    return max_word

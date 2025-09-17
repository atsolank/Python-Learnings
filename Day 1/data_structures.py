# Strings in Python
# A string is a sequence of characters inside quotes (" " or ' ').
# Strings are immutable (can’t be changed directly).

# text = "Python"
# print(text)

# Slicing means taking parts of a string using [start:end:step]
# print(text[0:4])   # Pyth
# print(text[:3])    # Pyt   (default start = 0)
# print(text[2:])    # thon  (default end = last)
# print(text[-3:])   # hon   (negative index = from end)
# print(text[::-1])  # nohtyP (reverse string)


# 📌 Case Methods
# word = "hello world"
# print(word.upper())    # HELLO WORLD
# print(word.lower())    # hello world
# print(word.title())    # Hello World
# print(word.capitalize())  # Hello world


# 📌 Search & Check
# text = "Python is fun"
# print(text.find("is"))     # 7  (index where found)
# print("fun" in text)       # True
# print("Java" not in text)  # True


# 📌 Replace & Strip
# msg = "   hello python   "
# print(msg.strip())              # "hello python" (removes spaces)
# print(msg.replace("python", "world"))  # hello world


# 📌 Splitting & Joining
# line = "apple,banana,cherry"
# fruits = line.split(",")    # ['apple', 'banana', 'cherry']
# print(fruits)

# new_line = "-".join(fruits)
# print(new_line)             # apple-banana-cherry

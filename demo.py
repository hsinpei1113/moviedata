print('hello world')
print("*" * 10)

course = "Python Programming"
print(len(course))
print(course[-1])
print(course[0:3])
print(course[:3])
print(course[0:])
print(course[:])

# escape sequence
course = "Python \"Programming"  # use\ to escape "function
print(course)

course = " python programming"
print(course.upper())
print(course.lower())
print(course.title())  # each word has capital alphabet
print(course.strip())  # remove space
print(course.find("pro"))  # find the index of pro
print(course.replace("p", "j"))
print("pro" in course)
print("bro" not in course)

# Number
print(10/3)
print(10//3)  # answer is INT
print(10*3)
print(10**3)  # 10的3次方
print(10 % 3)  # 餘數 remainder

# working with number
print(round(2.9))
print(abs(-2.9))  # absolute value

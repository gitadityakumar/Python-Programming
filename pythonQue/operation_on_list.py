marks = [98,99,100]
# looping on lists
for score in marks:
    print(score)


# operation on list
# append operation

marks.append(88)
print(marks)

# insert operation

marks.insert(0,97)
print(97 in marks)

# list length
print("the length of list is :")
print(len(marks))

# using while loop on lists

i = 0
while i < len(marks):
    print(marks[i])
    i += 1

# using clear
marks.clear()
print(marks)

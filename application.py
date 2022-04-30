# sent = "this is a sentence"
#
# print("Peter's sister's name's \"Anna\"")
#
# i = 250
# while len(str(i)) > 72:
#     i *= 2
# else:
#     i //= 2
# print(i)
#
# print(1, end= "**")
# print(1, end= " ")
# print(1, end= " ")
# print(1, end= " ")
#
# Val = 1
# Val2 = 0
# Val = Val ^ Val2
# Val2 = Val ^ Val2
# Val = Val ^ Val2
# print(Val)
#
# for i in range(1, 4, 2):
#     print("*")

# s = "Hello, Python!"
# print(s[-14:100])

# lst = ["A", "B", "C", 2, 4]
# del lst[0:-2]
# print(lst)

# s = 'python'
# for i in range(len(s)):
#     i = s[i].upper()
# print(s, end="")

def remainder(n1,n2):
    """

    :param n1: 1st user parameter
    :param n2:  2nd user parameter
    :return: returns the remainder of n1 divided by n2
    """
    return n1%n2

print(remainder(10,3))
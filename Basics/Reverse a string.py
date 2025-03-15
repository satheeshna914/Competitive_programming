#reverse a string
def reverse_string(s):
    return s[::-1]
s = "Hello, World!"
print(s)
print(reverse_string(s))

#2nd method- using loop
def reverse_2(s):
    str = ""    
    for i in s:
        str = i + str
    return str
s=str(input("Enter a string: "))
print("The original string is:",s)
print("The reversed string is:",reverse_2(s))

#3rd method- using recursion
def reverse_3(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])  # Takes  last char + reverse rest
print(reverse_string("hello"))  # Output: "olleh"




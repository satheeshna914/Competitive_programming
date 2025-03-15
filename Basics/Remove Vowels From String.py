def removevowels(s):
    vowels='aeiou'
    p=''
    for i in s:
        if i.lower() in vowels:
            continue
        else:
            p+=i
    return p
s="HEllo Worlf"
print(removevowels(s))
#2nd method
def remove_vowels(s):
    return ''.join(c for c in s if c.lower() not in 'aeiou')

# Example usage
print(remove_vowels("hello world"))  # Output: "hll wrld"

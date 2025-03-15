'''Input: num1 and num2 such that 0 <= num1 <= 99999999 and 0 <= num2 <= 9. You 
have to find number of occurences of input num2 in input num1 and return it with 
function int isOccured(int num1, int num2). 
Example: 
Input: num1= 199294, num2= 9
Output: 3 
Test Case 1: 
Input: 
1222212 
2 
Expected Output: 
5 
Test Case 2: 
Input: 
1001010 
0 
Expected Output: 
4 '''
def isOccured(num1, num2):
    if not (0 <= num1 <= 99999999) or not (0 <= num2 <= 9):
        return "Invalid input"
    count = 0
    while num1 > 0:
        if num1 % 10 == num2:  # Check last digit
            count += 1
        num1 //= 10  # Remove last digit
    return count
print(isOccured(199294, 9))   # Output: 3
print(isOccured(1222212, 2))  # Output: 5
print(isOccured(1001010, 0))

#2nd method----
def Occured(num1, num2):
    if not (0 <= num1 <= 99999999) or not (0 <= num2 <= 9):
        return "Invalid input"
    return str(num1).count(str(num2))
num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
print(Occured(num1, num2))

#3rd method----
def occur(n,m):
    return len(re.findall(str(m), str(n)))
# Test cases
print(isOccured(199294, 9))
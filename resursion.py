#Sum of n numbers
def sumOfnum(n):
    if n==0:
        return 0
    else:
        return n+sumOfnum(n-1)
print(sumOfnum(5))


#Factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))


#Palindrome
def palindrome(s,i,j):
    if i>=j:
        return True
    if s[i] != s[j]:
        return False
    else:
        return palindrome(s,i+1,j-1)

s = "madam"
i = 0
j = len(s)-1
print(palindrome(s,i,j))
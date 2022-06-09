#####
def isPalindrome (s):
    return s== s[::-1]

s = input("enter number or word ")
ans = isPalindrome(s)
if ans:
    print("yes")
else:
    print("no")
def pali(nums):
    revs="".join(reversed(nums))
    print(revs)
    rev=int(revs)
    num=int(nums)
    if rev == num:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")
pali(input("Please insert a number to be testered: "))
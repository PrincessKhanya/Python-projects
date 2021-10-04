def arm(numbers):  
    exp=len(numbers) 
    placeholder = 0
    
    numbers=int(numbers)
    numberse = numbers

    while numbers>0:
        placeholder=(placeholder)+((numbers%10)**exp)
        numbers=(numbers//10)
    print (placeholder)


    if placeholder == numberse :
        print("This is an armstrong number")
    else:
        print("This is not an armstrong number")

arm(input("Enter a number to be checked: "))
    
def prime(ents):
    ent=ents
    hold=0
    for i in range(2,(ent//2)):
        if (ent%i)==0:
            hold=1
            break
    if hold==1:
        print("This is not a prime number")
    else:
        print("This is a prime number")

prime(int(input("Please input a number to check if it is a prime number: ")))

def primes(ents):
    err=[1]
    ent=ents
    for i in range(1,(ent)):
        x=ent%i
        if x==0:
            err.append(int(ent/i))

    print(err)


primes(int(input("Please input a number to find its prime factors: ")))
def logical_phase(n):
    divisors =[1]
    while n%2==0:
        divisors.append(2)
        n=n//2
    factor = 3
    while factor*factor<=n:
        if n%factor==0:
            divisors.append(factor)
            n=n//factor
        factor =factor+2
    if n>2:
        divisors.append(n)
    return divisors
if __name__=="__main__":
    number=int(input("Enter the number :"))
    print(logical_phase(number))
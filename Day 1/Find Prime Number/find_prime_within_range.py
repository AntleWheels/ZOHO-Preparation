def logical_phase(n):
    if n==1 or n==0:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
if __name__=="__main__":
    start =int(input("Enter the starting number :"))
    end = int(input("Enter the ending number :"))
    prime_numbers = []
    for i in range(start,end+1):
        if logical_phase(i):
            prime_numbers.append(i)
    print(f"The prime numbers between the range {start} and {end} are : {prime_numbers}")
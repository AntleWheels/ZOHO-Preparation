def logical_phase(n):
    n= int(n)
    if n==1 or n==0:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
if __name__=="__main__":
    number = input("Enter the number :")
    if logical_phase(number) and logical_phase(number[::-1]):
        print(f"The given number {number} is a twisted prime number")
    else:
        print(f"The given number {number} is not a twisted prime number ")

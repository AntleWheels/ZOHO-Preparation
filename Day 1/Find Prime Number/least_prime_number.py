# Find the least prime number that can be added with first array element that makes them
# divisible by second array elements at respective index
def logical_phase(n):
    if n==1 or n==0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def core_logic(list1,list2):
    for i in list1:
        if (list2[0]+i)%list2[1] ==0:
            return i
    return "There is no such numbers which satisfies the rules"


if __name__=="__main__":
    numbers = list(map(int,input("Enter the numbers :").strip().split(",")))
    prime_numbers=[]
    for number in numbers:
        if logical_phase(number):
            prime_numbers.append(number)
    prime_numbers.sort()
    print(core_logic(prime_numbers,numbers))

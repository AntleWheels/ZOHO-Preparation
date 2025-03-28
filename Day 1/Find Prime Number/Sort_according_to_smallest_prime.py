def prime_logic(n):
    if n==1 or n==0 or n==2:
        return  False
    for i in range(2,n//2+1):
        if n%i==0:
            return i
    return  False
def sorting_function(arr):
    return sorted(arr,key=prime_logic)
if __name__=="__main__":
    numbers =list(map(int,input("Enter the numbers :").strip().split(",")))
    numbers =sorted(set(numbers))
    print(sorting_function(numbers))
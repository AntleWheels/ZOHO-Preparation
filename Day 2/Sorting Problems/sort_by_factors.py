def factor(n):
    count=0
    for i in range(2,n//2+1):
        if n%i==0:
            count=count+1
    return count
def sort_by_factors(arr):
    return sorted(arr,key =lambda x:(-factor(x),x))#(count of factors,element)
if __name__=="__main__":
    numbers =list(map(int,input("Enter the numbers :").strip().split(",")))
    print(sort_by_factors(numbers))
# sum of maximum subarray
def logical_phase(arr):
    current_sum =0
    max_sum =min(arr)
    for i in arr:
        current_sum=current_sum+i
        if i>current_sum:
            current_sum=i
        if current_sum>max_sum:
            max_sum=current_sum
    return max_sum
    
if __name__ =="__main__":
    numbers =list(map(int,input("Enter the numbers :").strip().split(",")))
    print(logical_phase(numbers))
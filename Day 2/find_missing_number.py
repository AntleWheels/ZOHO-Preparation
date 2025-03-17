def logical_phase(number):
    full_list=[num for num in range(number[0],number[-1])]
    missing_numbers=list(set(full_list)-set(number))
    return missing_numbers
if __name__=="__main__":
    numbers =list(map(int,input("Enter the numbers :").strip().split(",")))
    numbers = sorted(numbers)
    print(f"The missing numbers in the list {numbers} are",logical_phase(numbers))
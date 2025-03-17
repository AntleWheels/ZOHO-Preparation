def logical_phase(n):
    return sorted(set(n))
if __name__=="__main__":
    numbers=list(map(int,input("Enter the numbers :").strip().split(",")))
    print(f"the sorted form of the list {numbers} is ",logical_phase(numbers))


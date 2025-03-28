def logical_phase(n):
    set_of_numbers = sorted(set(n))
    return set_of_numbers
if __name__ =="__main__":
    numbers = list(map(int, input("Enter the numbers :").strip().split(",")))
    print(logical_phase(numbers))
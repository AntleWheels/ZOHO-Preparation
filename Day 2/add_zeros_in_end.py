def logical_phase(a):
    zeros_list=[]
    non_zeros_list=[]
    for i in a:
        if i==0:
            zeros_list.append(i)
        else:
            non_zeros_list.append(i)
    return non_zeros_list+zeros_list
if __name__=="__main__":
    numbers = list(map(int,input("Enter the numbers :").strip().split(",")))
    print(f"The entered list is {numbers} and the list is",logical_phase(numbers))
def logical_phase(n):
    reversed_list=[]
    for i in n[::-1]:
        reversed_list.append(i)
    return reversed_list
if __name__ =="__main__":
    numbers = list(map(int,input("Enter the numbers :").strip().split(",")))
    print(f"The reversed form for the list{numbers} is ",logical_phase(numbers))
def logical_phase(n):
    even_list =[num for num in n if num%2==0]
    odd_list =[num for num in n if num%2!=0]
    even_list =sorted(even_list)
    even_list.reverse()
    odd_list =sorted(odd_list)
    return even_list,odd_list

if __name__ =="__main__":
    numbers =list(map(int,input("Enter the numbers :").strip().split(",")))
    print(f"The sorted form of the list {numbers} are",logical_phase(numbers))

from collections import Counter
def logical_phase(n):
    counter_value = Counter(n)
    decencending_order =sorted(n,key=lambda x: (counter_value[x],x),reverse=True)
    return decencending_order
if __name__ =="__main__":
    numbers = list(map(int,input("Enter the numbers :").strip().split(",")))
    print(f"The sorted form of the list{numbers} is ",logical_phase(numbers))
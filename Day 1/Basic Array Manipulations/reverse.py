if __name__ =="__main__":
    numbers = list(map(int,input("Enter the numbers :").strip().split(",")))
    print(f"The reversed form for the list{numbers} is ",numbers[::-1])

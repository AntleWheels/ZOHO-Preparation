def logical_phase(l,b):
    for i in range(l):
        print(" * "*b)
if __name__ =="__main__":
    length =int(input("Enter the length of the rectangle :"))
    bredth =int(input("Enter the bredth of the rectangle :"))
    logical_phase(length,bredth)
def logical_phase(n):
    for i in range(n+1):
        print(" "*(n-i) ,"* "*i)
if __name__ =="__main__":
    height = int(input("Enter the height of the triangle :"))
    logical_phase(height)


#Add the space first and then add the *
#gradually decrease the space and increase the *
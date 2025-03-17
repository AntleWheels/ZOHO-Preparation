def logical_phase(n):
    for i in range(n+1):
        print(" "*(n-i),"* "*i)
    for j in range(n,0 ,-1):
        print(" "*(n-j),"* "*j)
if __name__ =='__main__':
    height = int(input("Enter the height of the triangle :"))
    logical_phase(height)
# for i in  range(10 ,0 ,-1):
#     print(" "*(10-i) ," *"*i)
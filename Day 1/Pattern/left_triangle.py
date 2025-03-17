# for i in range(10):
#     print("  "*10 , " * "*10)
def logical_phase(n):
    for i in range(n):
        print("  " * (n-i -1) + "* " * (i + 1))
if __name__ =="__main__":
    height =int(input("Enter the height of the triangle :"))
    logical_phase(height)

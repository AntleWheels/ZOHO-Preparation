def logical_phase(num1,num2):
    final_number = ""
    for i in str(num1):
        final_number += str(int(i)+int(num2))
    return final_number
if __name__ =="__main__":
    number1 =int(input("Enter the number :"))
    number2 =int(input("Enter the second number :"))
    print(logical_phase(number1,number2))
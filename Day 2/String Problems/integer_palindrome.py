def logical_phase(number):
    original_number=number
    reversed_number=0
    if number<0:
        return "The number must be greater than 0"
    else:
        while number>0:
            last_number = number%10
            reversed_number=reversed_number*10+last_number
            number =number//10
    if reversed_number == original_number:
        return "a palindrome"
    else:
        return " not a palindrome"
if __name__=="__main__":
    number=int(input("Enter the number to check wheather the number is palindrome or not :"))
    print(f"The entered number {number} is",logical_phase(number))
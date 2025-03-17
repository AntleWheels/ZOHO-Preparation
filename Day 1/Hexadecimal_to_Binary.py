def hex_to_binary(n):
    n =n.upper()
    hexa={
        '0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'A':'1010',
        'B':'1011',
        'C':'1100',
        'D':'1101',
        'E':'1110',
        'F':'1111'
    }
    binary =""
    for i in n:
        binary =binary + hexa[i]
    return binary

if __name__ =="__main__":
    hexa = input("Enter the hexadecimal number :")
    print("The binary equivalent of the hexadecimal number is ",hex_to_binary(hexa))
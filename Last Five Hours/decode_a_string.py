# Decode a string
numbers ={
    'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26
}
def encode_string(s):
    if s.isalpha():
        result =""
        for i in s:
            if i in numbers.keys():
                if numbers[i]>=10:
                    result+= " "+str(numbers[i])
                else:
                    result+=str(numbers[i])
        return result
    if s.isdigit():
        return decode_string(s)
    else:
        return "Special Charectors are able to decoded"
def decode_string(s):
    result=""
    list_variable = list(map(int, s.split()))
    for num in list_variable:
        for key, value in numbers.items():
            if value == num:
                result+=key
    return result 
if __name__ =="__main__":
    string =input("Enter the string :").strip().upper()
    if string.isalpha():
        print(encode_string(string))
    else:
        print(decode_string(string))
def logical_phase(n):
    n=list(n)
    string_list=[char for char in n if char.isalpha()]
    reversed_list =string_list[::-1]
    final_string =""
    initial_index =0
    for i in n:
        if i.isalpha():
            final_string=final_string+reversed_list[initial_index]
            initial_index=initial_index+1
        else:
            final_string=final_string+i
    return final_string

if __name__=="__main__":
    letter =input("Enter the string to reverse :")
    print(f"The reversed form of the word {letter} is",logical_phase(letter))
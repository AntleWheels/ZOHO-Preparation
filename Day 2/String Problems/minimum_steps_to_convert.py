def logical_phase(n):
    count =0
    i=0
    length=len(n)
    while i<=length-2:
        if n[i]=="X":
            count=count+1
            i=i+2
        else:
            i=i+1
    return count
if __name__=="__main__":
    word=input("Enter the word :")
    print(f"The minimum steps to convert the word {word} is",logical_phase(word))
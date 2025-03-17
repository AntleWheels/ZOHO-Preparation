def logical_phase(a,b):
    i,j =0,0
    while i <len(a) and j<len(b):
        if a[i]==b[j]:
            i+=1
        j+=1
    return i==len(a)
if __name__ == "__main__":
    word1= input("Enter the first word :")
    word2=input("Enter the second word :")
    print(logical_phase(word2,word1))


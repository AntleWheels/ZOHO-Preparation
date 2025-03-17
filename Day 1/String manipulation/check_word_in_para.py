def logical_phase(a,b):
    if b in a:
        return "Present in the list"
    else:
        return "Not present in the list"
if __name__ =="__main__":
    paragraph =input("Enter a paragraph :").lower().split()
    word =input("Enter the word to search :").lower()
    print(f"The entered word {word} is ",logical_phase(paragraph,word))
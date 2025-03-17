def logical_session(n):
    if n==n[::-1]:
        return "Its a palindrome string"
    else:
        return "Its not a palindrome string"
if __name__=="__main__":
    word = input("Enter the word to check wheather the word is palindrome or not :")
    print(f"The entered wrod :{word}",logical_session(word))
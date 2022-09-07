def stringtoint(word):
    new_String = "";
    for i in range(len(word)):
        if word[i] == " ":   
            continue
        new_String += word[i]
    return new_String == word[::-1]
    
def main():
    print (stringtoint("   -42"))
    print (stringtoint("303"))
    print (stringtoint("66"))
    






if __name__ == "__main__":
    main()
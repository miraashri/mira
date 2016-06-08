def main():
    string = (raw_input("Enter the string : "))
    integer = str_to_int(string)
    print("The string and the integer are : %s and %d"%(string,integer))

def str_to_int(ex):
    counter = ans = 0
    for i in reversed(ex):
        ans += (ord(i) - 48) * 10 ** counter
        counter += 1
    return ans

if __name__ == '__main__':
    main()

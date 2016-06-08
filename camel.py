def main():
    string = (raw_input("Enter a string : "))
    a = string.split()
    for i in range(len(a)):
        x = a[i]
        a[i] = x.capitalize()
    ans = a[0]
    for i in range(1,len(a)):
        ans += a[i]
    print("The CamelCase of converted string is %s"%ans)
main()

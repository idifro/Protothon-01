import string

if __name__=='__main__':
    
    str = input("Enter the string\n")
    
    print("The possible text formatter operations are:")
    print("1.All cops 2.Small caps 3.Title Caps 4.Start caps")
    op = int(input("Enter the operation number to perform"))
    
    if(op==1):
        print(str.upper())
    if(op==2):
        print(str)
    if(op==3):
        print(str.title())
    if(op==4):
        print(str.capitalize())
        
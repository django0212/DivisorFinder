import os

def main():
    dic=[]
    n=(int(input("Enter Number: ")))
    print('\n')
    for x in range(1,n+1):
        if(n%x==0):
            print(x)
            dic.append(x)
    print('\n')
    print('Total number of terms: %d\n' % (len(dic)))
    chc = input('Again (press n to quit)?')
    if chc != 'n':
        os.system('cls')
        main()
    else:
        exit()  
main()

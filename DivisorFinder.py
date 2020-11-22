import os

def main():
    dic=[]
    y=0
    n=(int(input("Enter Number: ")))
    print('\n')
    for x in range(1,n+1):
        if(n%x==0):
            print(x)
            dic.append(x)
    for y in range(len(dic)):
                y+=1
    print('\n')
    print('Total number of terms: %d\n' % (y))
    chc = input('Again (press n to quit)?')
    while chc != 'n':
        os.system('clear')
        main()
    else:
        exit()  
main()

add_str = []
even_str = []

N = int (input())
for _ in range(N):
    add_str=[]
    even_str=[]
    str = input()
    ''' print("string=",str,"length=",len(str)) '''
    for i in range(len(str)):
        if (i%2 == 0):
            even_str.append(str[i])
        else:
            add_str.append(str[i])
    for eve_c in even_str:
        print(eve_c,end="")
    print(end=" ")
    for add_c in add_str:
        print(add_c,end="")
    print(end="\n")
    


def sum(list):
    total =0
    print("even numbers are:",end="")
    for i in list:
        if (i % 2 == 0):
            print(i,end=" ")
            total = total + i
    return total
if __name__ =="__main__":
 print ("\nsum of even number :",sum([1,2,3,4,5,6,7,8]))

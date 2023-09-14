import csv,os
def csv_file(f_name="input.csv"):
 f_obj = open(f_name,"r",newline="")
 file  = csv.reader(f_obj)
 data = list(file)
 for line in data:
    for word in line:
        print(word,"\t",end="")
    print()
csv_file()
csv_file("input.csv")
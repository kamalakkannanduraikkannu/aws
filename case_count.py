def case_count(string="Hai"):
    ucount = 0
    lcount = 0
    for i in string:
        if (i.islower()):
            lcount = lcount+1
        if(i.isupper()):
            ucount = ucount + 1
    print("lower case count:",lcount,"upper case count:",ucount)

case_count("HelloWorld how ARE")
case_count()
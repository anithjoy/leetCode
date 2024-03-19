def triangle():

    for i in range(10):
        star = "*"
        line = " "*(10 - i) + star + " "*i*2 + star
        print(line)

    lastLine = " " + star * 20
    print(lastLine)
        

triangle()
import statistics

def readNumbersFromFile(x):
    a=open(x,"r")
    b=0
    c=0
    lista=[]
    for i in a:
        b=b+int(i)
        c=c+1
        list.append(int(i))
    st=statistics.stdev(list)
    print("The total of the value is: ",b)
    print("The number of the value is: ,",c)
    print("The arithmetic mean of the values is: ",(b/c))
    print("The standard deviation of the values is: ",st)

readNumbersFromFile("cachorros.txt")

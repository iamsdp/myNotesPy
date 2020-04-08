    L = myfile.read()
    #Remove comments /* comments */
    L = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,L)

    lines = L.split(';')
    # print(L)

    #Remove extra spaces from left and right of string
    lines = [line.strip() for line in lines]

    #Remove extra unnecessary spaces in line : "Create     table" ==> "Create table"
    lines = [re.sub(' +', ' ', line) for line in lines]

    #Remove null char from lines i.e. remove empty line from file
    lines = [i for i in lines if i]

def docFile():
    file = open('input.txt' , 'r' ,encoding='utf-8')
    for line in file:
        print(line.strip())
    file.close()
docFile()
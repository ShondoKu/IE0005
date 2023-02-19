from os import path
file_path = path.abspath('')
dir_path = path.dirname(file_path)
blocklist_file_path = path.join(dir_path,'blocklist.txt')
visitorlist_file_path = path.join(dir_path,'visitorlist.txt')


try:
    v = open('visitorlist.txt')
    visitors = v.read().split('\n')
    print(visitors)
    for f in range(0,len(visitors)):
        print(str(f+1) + '. ' + str(visitors[f]))
    choice = int(input('Which user would you like to block?'))

    b = open('blocklist.txt','a+')
    print(b.readlines())
    for x in b.readlines():
        if x != visitors[choice - 1]:
            b.write('\n'+ visitors[choice - 1])
    print(b.readlines())


except FileNotFoundError:
    if path.exists(blocklist_file_path) == False:
        print('File blocklist.txt not found')
    elif path.exists(visitorlist_file_path) == False:
        print('File visitorlist.txt not found')
else:
    v.close()
    b.close()
    
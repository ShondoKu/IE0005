from os import path
file_path = path.abspath(__file__) # full path of your script
dir_path = path.dirname(file_path) # full path of the directory of your script
blocklist_file_path = path.join(dir_path,'blocklist.txt')
visitorlist_file_path = path.join(dir_path,'visitorlist.txt')

try: 
    v=open('visitors.txt')
    visitors=v.read().split('\n')

    for x in visitors:
        if x == "alice@wonderland.co.uk":
            b=open('blocklist.txt','a')
            b.write("\n"+x)
            b.close()

    '''b=open('blocklist.txt')
    for u in b.readlines():
        print(u)'''

except FileNotFoundError:
    if path.exists(blocklist_file_path) == False:
        print('File blocklist.txt not found!')
    elif path.exists(visitorlist_file_path) == False:
        print('File visitorlist.txt not found!')
else:
    v.close()
    b.close()
    
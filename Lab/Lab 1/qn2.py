from os import path
file_path = path.abspath(__file__) # full path of your script
dir_path = path.dirname(file_path) # full path of the directory of your script
blocklist_file_path = path.join(dir_path,'blocklist.txt')
visitorlist_file_path = path.join(dir_path,'visitorlist.txt')


try: 
    b=open('blocklist.txt')
    v=open('visitorlist.txt')
    
    visitors=v.read().split('\n')
    blocklist=b.read().split('\n')

    blockname=[]

    for x in visitors:
        for y in blocklist:
            if x == y:
                blockname.append(x)

    print(str(len(visitors)) + ' number of visitors today.')
    for u in blockname:
        print(u + " has been denied access.")
        
except FileNotFoundError:
    if path.exists(blocklist_file_path) == False:
        print(path.exists(blocklist_file_path))
        print('File blocklist.txt not found!')
    elif path.exists(visitorlist_file_path) == False:
        print('File visitorlist.txt not found!')
else:
    b.close()
    v.close()
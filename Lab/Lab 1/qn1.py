try: 
    f=open('blocklist.txt')
    username=[]
    
    for x in f.readlines():
        if x not in username:
            username.append(x)
        else:
            print('Username exist!')

    for u in username:
        print(u)

except FileNotFoundError:
    print('File blocklist.txt not found!')
else:
    f.close()
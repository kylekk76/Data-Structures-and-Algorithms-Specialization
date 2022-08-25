# This will not work for the assignament as you need some more simple, but i thought was better in this way

def inputmain():
    loop=True
    while loop:
        try:
            text= input("introduce two numbers or stop to finish: ")
            a,b = map(int,text.split())
            print(a+b)   
        except:
            if text == "stop": loop=False
            else: print("try again")
              
    

if __name__ == '__main__':
    inputmain()

print("welcome to my library\n1.Display book\n2.Lend a book\n3.Add a book\n4.Return a book")
aa="welcome to my library\n1.python\n2.java"
a=["html","css","boot strap","java script","react","python","java"]
a1=["html","css","boot strap","java script","react","python","java"]

abc=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class library():
    def __init__(self,a):
        self.a=a
        # self.b=b
    def display_index(self):
       print("welcome to my library\n1.display book\n2.lend a book\n3.add a book\n4.Return a book")
        
    def lead(self):
        a=1
        for i in self.a:
            print(f"{a} {i}")
            a+=1
    def _display_book(self):
        a=1
        for i in self.a:
            print(f"{a} {i}")
            a+=1
    def add_book(self):
        
        # print(f"{self.a}")
        a=1
        for i in self.a:
            print(f"{a} {i}")
            a+=1

        
    def _return_book(self):
        a=1
        for i in self.a:
            print(f"{a} {i}")
            a+=1
        
        
        
        
                
        
        
human=library(a)
# human2=library(user__input)

while True:
    _user_input=input("Your Choice")
    if _user_input=="" :
                while True:
                    _user_input=input("Your choice")
                    if _user_input!="":
                        break
    # if _user_input ==str:
    if _user_input in abc:
        while True:
            _user_input=input("your choice must be a number")
            if _user_input=="":
                while True:
                    _user_input=input("your choice must be a number")
                    if _user_input!="":
                        break


            if _user_input not in abc:
                break

    
        


    _user_input=int(_user_input)
    # if _user_input in int:
    #     _user_input=int(_user_input)

    
         
    if _user_input ==1:
        human._display_book()
        _user_sec=input("c for Back and q for Qict")
        if _user_sec=="":
            while True:
                _user_sec=input("c for back and q for Qict")
                if _user_sec!="":
                    break
        if _user_sec!="c" and _user_sec!="q":
            while True:
                _user_sec=input("c or q")
                if _user_sec =="c" or _user_sec=="q":
                    break
                
        if _user_sec=="c":
            human.display_index()
        elif _user_sec=="q":
        
            break
        
            
        

    elif _user_input==2:
        human.lead()
        print("c for Back")
        _user_buy=input("Enter book name")
        if _user_buy=="":
            while True:
                _user_buy=input("Enter book name")
                if _user_buy!="":
                    break
        

        if _user_buy =="c":
            human.display_index()
        if _user_buy!="c":

            if _user_buy in a:
                a.remove(_user_buy)
                print(f"keep it's safe and Enjoy your {_user_buy} book")
                _user_secc=input("c for Back and q for Qict")
                if _user_secc!="c" and _user_secc!="q":
                    while True:
                        _user_secc=input("c or q")
                        if _user_secc =="c" or _user_secc=="q":
                            break

                if _user_secc=="":
                    while True:
                        _user_secc=input("c for Back and q for Qict")
                        if _user_secc!="":
                            break
                        # elif _back=="c":
                        #     human.display_index()
                if _user_secc=="c":
                    human.display_index()
                elif _user_secc=="q":
                    break
            elif _user_buy not in a:
                print(f"U selected book  {_user_buy} is not in library")
                _back=input("c for Back and q for Quit")
                if _back!="c" and _back!="q" :
                    while True:
                        _back=input("c or q")
                        if _back =="c" :
                            break
                        elif _back=="q":
                            break
                if _back=="":
                    while True:
                        _back=input("c for Back and q for Quit")
                        if _back!="":
                            break
                        # elif _back=="c":
                        #     human.display_index()
                elif _back=="c":
                    human.display_index()
                elif _back=="q":
                    break

            # if user_secc=="c":
            #     human.display_index()
            # elif user_secc=="q":
            #     break
        # elif _user_buy=="c":
        #     human.display_index()
            # user_secc=input("c for continue and q for qict")
            
        
        
    elif _user_input==3: 
        print("Enter the name of the book to add to the library")
        print("c for Back")
        user__input=input("Book Name")
        if user__input=="":
            while True:
                user__input=input("Book Name")
                if user__input!="":
                    break
                elif user__input=="c":
                    human.display_index()
        if user__input=="c":
            human.display_index()
        else:
            a.append(user__input)
            a1.append(user__input)
            print(f"Your book {user__input} is successfully added in our library")
            human.add_book()
            user_secc=input("c for Back and q for Qict")
            if user_secc=="":
                    while True:
                        user_secc=input("c for Back and q for Qict")
                        if user_secc !="":
                            break
            if user_secc=="c":
                human.display_index()
            elif user_secc=="q":
                break
        
        
                        
        
        
        
                    
         
         
         
    elif _user_input==4:
        print("c for Back and q for Qict")
        _user_return_book=input("Enter the book name u want to return \n")
        # human2=library(_user_return_book)
        
        if _user_return_book =="":
            while True:
                _user_return_book=input("Enter the book name u want to return \n")
                if _user_return_book!="":
                    break
        if _user_return_book=="c":
            human.display_index()
        elif _user_return_book=="q":
            break

        #    

        
                      
        elif _user_return_book in a1 and _user_return_book not in a:
            if _user_return_book=="c" or _user_return_book=="q":
                break
            else:
                print(f"Returned book {_user_return_book} is added in our library ")
                a.append(_user_return_book)
                user_secc=input("c for Back and Q for Qict")

                if user_secc=="":
                    while True:
                        user_secc=input("c for Back and q for Qict")
                    if user_secc !="":
                        break
            if user_secc!="c" and user_secc!="q":
                while True:
                    user_secc=input("c or q")
                    if user_secc =="c" or user_secc=="q":
                        break
                    
            if user_secc=="c":
                human.display_index()
            elif user_secc=="q":
                break
                human._return_book()

            
        else:
            print("Return book name is not in our library list")
            user_secc=input("c for Back and q for Qict")
            if user_secc=="":
                while True:
                    user_secc=input("c for Back and q for Qict")
                    if user_secc !="":
                        break
            if user_secc!="c" and user_secc!="q":
                while True:
                    user_secc=input("c or q")
                    if user_secc =="c" or user_secc=="q":
                        break
                    
            if user_secc=="c":
                human.display_index()
            elif user_secc=="q":
                break

        

    















    # print(_user_input)
    # if _user_input==int :
    #     _user_input=int(_user_input)
    #     # print(_user_input)
    #     _user_input=input("Your Option")
    #     if(_user_input=="c"):
    #        human.display_index()
    #     elif (_user_input ==2):
    #        human._display_book()



    


from view import view
from model import model
from msvcrt import getch

v = view(0,0,0)
m = model(0)

class controller:
    def __init__(self,id1):
        self.id1 = id1      # id1 là id username đăng nhập vào hệ thống
    def register(self):
        v.dangki()
        m.open()
        id = m.checkUserInDB(v.username)
        if(id == 0):
            m.dangki(v.username, v.password, v.city)
            print("dang ki thanh cong")

        else:
            print("username da ton tai trong he thong")

    def login(self):
        v.login()
        m.open()
        id = m.login(v.username,v.password)
        if(id>0):
            print("dang nhap thanh cong")
            self.id1 = id       #id1 = id v.username
            print("==========")
            self.loginThanhCong()


        else:
            print("username hoac password khong dung")

    def addFriend(self):
        id = 0
        id1 = self.id1
        v.nhapUsername()
        m.open()
        id = m.checkUserInDB(v.username)
        if(id>0):
            isFriend = m.checkFriendAndBlock(id1,id)
            if(isFriend == 1):
                print("username da co trong list friend")
            elif(isFriend==0):
                print("khong the them username nay vao list friend")
            else:
                m.addFriend(id1,id)
                print("add friend successfully")



        else:
            print("username khong ton tai")

    def block(self):
        v.nhapUsername()
        m.open()
        id = m.checkUserInDB(v.username)
        if(id > 0):
            isFriend = m.checkFriendAndBlock(self.id1,id)
            if(isFriend == 1):
                m.friendToBlock(self.id1,id)
                print("block successfully")
            elif(isFriend == 0):
                print("khong tim thay username")
            else:
                m.block(self.id1,id)
                print("block successfully")
        else:
            print("username khong ton tai")

    def showFriend(self):
        m.open()
        m.showFriend(self.id1)
        listF = m.listF
        for x in range(len(listF)):
            print(x+1,listF[x])
        print("press ctrl + c to order list friend by city")
        print("press ctrl + b to back")
        key = ord(getch())

        while True:
            if (key == 3):
                self.showFriendByCity()
                break
            elif (key == 2):
                self.loginThanhCong()
                break
            else:
                print("press ctrl + c to order list friend by city")
                print("press ctrl + b to back")
                print("==========")
                key = ord(getch())



    def showFriendByCity(self):
        m.open()
        m.showCity(self.id1)
        for x in m.listCity:
            print(x)
            m.showFriendByCity(self.id1,x)


    def sendMess1(self):
        v.nhapUsername()
        m.open()
        id = m.checkUserInDB(v.username)
        if(id > 0):
            isFriend = m.checkFriendAndBlock(self.id1,id)
            if(isFriend == 0):
                print("khong the gui tin nhan cho username nay")
            else:
                print("to: ",v.username)
                v.sendMess()
                m.sendMess(self.id1,id,v.mess)
                print("send messenger successfully")
        else:
            print("username khong hop le")
    def sendMess2(self):
        id = 0
        m.open()
        m.showFriend(self.id1)
        listF = m.listF
        for x in range(len(listF)):
            print(x + 1, listF[x])
        print("======")
        print("nhap id: ")
        id = int (input())
        if(id<0 or id>len(listF)):
            print("lua chon khong hop le")

        else:
            print("to: ",listF[id-1])
            id2 = m.checkUserInDB(listF[id-1])
            v.sendMess()
            m.sendMess(self.id1,id2,v.mess)
            print("send messenger successfully")

    def sendMess(self):
        print("press ctrl + N to typing username")
        print("press ctrl + L to show list Friend")
        key = ord(getch())
        while True:
            if (key == 14):
                self.sendMess1()
                break
            elif (key == 12):
                self.sendMess2()
                break
            elif (key == 2):
                self.loginThanhCong()
                break
            else:
                print("press ctrl + N to typing username")
                print("press ctrl + L to show list Friend")
                print("press ctrl + B to back")
                print("==========")
                key = ord(getch())



    def sent(self):
        id = 0
        print("====== gan day ======")
        m.open()
        m.showTo(self.id1)
        for x in range(len(m.listTo)):
            print(x+1,m.listTo[x])
        print("======")
        print("nhap id: ")
        id = int(input())
        if(id<0 or id >len(m.listTo)):
            print("lua chon khong hop le")
        else:
            print("mess to: ",m.listTo[id-1])
            print("==========")
            id2 = m.checkUserInDB(m.listTo[id-1])
            m.sent(self.id1,id2)
            print("press ctrl + R to resend")
            print("press ctrl + B to back")
            key = ord(getch())
            while True:
                if (key == 18):

                    m.sendMess(self.id1, id2, m.sentM)
                    print("==========")
                    print("resend sucessfully")
                    break
                elif (key == 2):
                    self.loginThanhCong()

                else:
                    print("press ctrl + R to resend")
                    print("press ctrl + B to back")
                    print("==========")
                    key = ord(getch())



    def inbox(self):
        id = 0
        print("====== gan day ======")
        m.open()
        m.showFrom(self.id1)
        for x in range(len(m.listFrom)):
            print(x + 1, m.listFrom[x])
        print("======")
        print("nhap id: ")
        id = int(input())
        if (id < 0 or id > len(m.listFrom)):
            print("lua chon khong hop le")
        else:
            print("mess from: ", m.listFrom[id - 1])
            print("==========")
            id2 = m.checkUserInDB(m.listFrom[id - 1])
            m.inbox(self.id1, id2)
            print("press ctrl + R to rep inbox")
            key = ord(getch())
            while True:
                if (key == 18):
                    v.sendMess()
                    m.sendMess(self.id1, id2, v.mess)
                    print("send messenger successfully")
                    break
                elif(key == 2):
                    self.loginThanhCong()
                    break
                else:
                    print("press ctrl + R to rep inbox")
                    print("press ctrl + B to back")
                    print("==========")
                    key = ord(getch())






    def loginThanhCong(self):
        luachon = 0
        while True:
            v.loginThanhCong()
            luachon = int(input())
            if (luachon < 0 or luachon > 8):
                print("lua chon khong hop le")
            else:
                if (luachon == 1):
                    c.addFriend()
                elif (luachon == 2):
                    c.block()
                elif (luachon == 3):
                    c.showFriend()
                elif(luachon==4):
                    c.sendMess()
                elif(luachon == 5):
                    c.sent()
                elif(luachon==6):
                    c.inbox()
                elif(luachon == 7):
                    self.start()



    def start(self):
        while True:
            v.menu1()
            luachon = int(input())
            if (luachon <= 0 or luachon > 3):
                print("lua chon khong hop le")
            else:
                if (luachon == 1):
                    c.register()
                elif (luachon == 2):
                    c.login()
                elif (luachon == 3):
                    exit(0)




c = controller(0)
c.start()






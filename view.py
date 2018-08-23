
class view:
    def __init__(self,username,password,city):
        self.username = username
        self.password = password
        self.city = city
        self.mess = 0
    def dangki(self):
        print("nhap username: ")
        self.username = input()
        print("nhap password: ")
        self.password = input()
        print("nhap city: ")
        self.city = input()
    def thongbao(self):
        print("dang ki thanh cong")
        print("\n")
        print("thong tin vua nhap vao la: \n")
        print("username: "+self.username)
        print("\n")
        print("password: "+self.password)
        print("\n")
        print("city: "+self.city)

    def login(self):
        print("username: ")
        self.username = input()
        print("password: ")
        self.password = input()

    def nhapUsername(self):
        print("nhap username: ")
        self.username = input()
    def loginThanhCong(self):
        print("==========")
        print("1. add friend")
        print("2. block")
        print("3. show friend")
        print("4. send Mess")
        print("5. sent")
        print("6. inbox")
        print("7. logout")
    def sendMess(self):
        print("soan tin: ")
        self.mess = input()

    def showTo(self):
        print("====== gan day ======")
    def menu1(self):
        print("====== Menu ======")
        print("1. register")
        print("2. login")
        print("3. exit")
        print("nhap lua chon: ")






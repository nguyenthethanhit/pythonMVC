import sqlite3
import time
class model:
    def __init__(self,db):
        self.db = db
        self.listF = []     # danh sách bạn bè
        self.listTo = []     # danh sách người nhận
        self.listFrom = []  # danh sách người nhận
        self.listCity = []  # danh sách thành phố
        self.sentM = 0      # tin nhắn cuối cùng đã gửi
    def open(self):
        self.db = sqlite3.connect('chat.db')
    def dangki(self,username,password,city):
        db = self.db
        cursor = db.cursor()
        cursor.execute('''insert into user1(username,password,city) values(?,?,?)''',(username,password,city))
        db.commit()

    def checkUserInDB(self,username):
        id =0
        db = self.db
        cursor = db.cursor()
        cursor.execute('''select id from user1 where username = ? ''',(username,))
        while True:

            row = cursor.fetchone() #lay ra 1 hang

            if row == None:
                break
            id = row[0]

        return id

    def login(self,username,password):
        id =0
        db = self.db
        cursor = db.cursor()
        cursor.execute('''select id from user1 where username = ? and password = ?''',(username,password))
        while True:

            row = cursor.fetchone() #lay ra 1 hang

            if row == None:
                break
            id = row[0]

        return id

    def checkFriendAndBlock(self,id1,id2):
        isFriend = -1
        db = self.db
        cursor = db.cursor()
        cursor.execute('''select isFriend from friend1 where (id1 = ? and id2 = ?) or (id1 = ? and id2 = ?)''',(id1,id2,id2,id1))
        while True:

            row = cursor.fetchone() #lay ra 1 hang

            if row == None:
                break
            isFriend= row[0]

        return isFriend


    def addFriend(self,id1,id2):
        db = self.db
        cursor = db.cursor()
        cursor.execute('''insert into friend1(isFriend, id1, id2 ) values(1,?,?) ''', (id1,id2))
        db.commit()

    def block(self,id1,id2):
        db = self.db
        cursor = db.cursor()
        cursor.execute('''insert into friend1(isFriend,id1,id2) values(0,?,?)''',(id1,id2))
        db.commit()

    def friendToBlock(self,id1,id2):
        db = self.db
        cursor = db.cursor()
        cursor.execute('''update friend1 set isFriend = 0 where (id1 = ? and id2 = ?) or (id1 = ? and id2 = ?)''',(id1,id2,id2,id1))
        db.commit()

    def showFriend(self,id1):
        self.listF.clear()
        db = self.db
        cursor = db.cursor()
        cursor.execute('''select user1.username from user1, friend1 where (isFriend = 1 and friend1.id1 = ? and friend1.id2 = user1.id) or (isFriend = 1 and friend1.id2 = ? and friend1.id1 = user1.id) order by friend1.time desc ''',(id1,id1))
        while True:

            row = cursor.fetchone() #lay ra 1 hang

            if row == None:
                break

            self.listF.append(row[0])

    def sendMess(self,id1,id2,mess):
        localtime = time.asctime(time.localtime(time.time()))
        db = self.db
        cursor = db.cursor()
        cursor.execute('''insert into mess1 (id1,id2,mess,time,seen) values(?,?,?,?,'sent')''',(id1,id2,mess,localtime))
        db.commit()
        self.updateTuongTac(id1,id2)    # update time tương tác để hiện thị danh sách bạn bè theo thời gian tương tác cuối cùng

    def sent(self,id1,id2):
        db = self.db
        cursor = db.cursor()
        cursor.execute('''select mess,time,seen from mess1 where id1 = ? and id2 = ?''',(id1,id2))
        while True:

            row = cursor.fetchone() #lay ra 1 hang

            if row == None:
                break

            print(row[0],row[1],row[2])
            self.sentM = row[0]     # tin nhắn đã gửi cuối cùng

    def showTo(self,id1):
        self.listTo.clear()
        db = self.db
        cursor = db.cursor()
        cursor.execute('''select distinct user1.username from user1,mess1 where mess1.id1 = ? and mess1.id2 = user1.id''', (id1,))
        while True:

            row = cursor.fetchone()  # lay ra 1 hang

            if row == None:
                break

            self.listTo.append(row[0])

    def showFrom(self,id1):
        self.listFrom.clear()
        db = self.db
        cursor = db.cursor()
        cursor.execute('''select distinct user1.username from user1,mess1 where mess1.id2 = ? and mess1.id1 = user1.id''', (id1,))
        while True:

            row = cursor.fetchone()  # lay ra 1 hang

            if row == None:
                break

            self.listFrom.append(row[0])

    def inbox(self,id1,id2):
        db = self.db
        cursor = db.cursor()
        cursor.execute('''select mess,time from mess1 where id1 = ? and id2 = ?''', (id2, id1))
        while True:

            row = cursor.fetchone()  # lay ra 1 hang

            if row == None:
                break

            print(row[0],row[1])
        self.updateSeen(id1,id2)    #update trạng thái tin nhắn sent -> seen

    def updateSeen(self,id1,id2):
        db = self.db
        cursor = db.cursor()
        cursor.execute('''update mess1 set seen = 'seen' where id1 = ? and id2 = ?''',(id2,id1))
        db.commit()

    def updateTuongTac(self,id1,id2):
        localtime = time.asctime(time.localtime(time.time()))
        db = self.db
        cursor = db.cursor()
        cursor.execute('''update friend1 set time = ? where (id1 = ? and id2 = ?) or (id1 = ? and id2 = ?)''', (localtime,id1, id2,id2,id1))
        db.commit()

    def showCity(self,id1):
        self.listCity.clear()
        db = self.db
        cursor = db.cursor()
        cursor.execute('''select distinct user1.city from user1 ,friend1 where friend1.isFriend = 1 and ((friend1.id1 = ? and friend1.id2 = user1.id) or (friend1.id2 = ? and friend1.id1 = user1.id))''',(id1,id1))
        while True:

            row = cursor.fetchone()  # lay ra 1 hang

            if row == None:
                break

            self.listCity.append(row[0])
    def showFriendByCity(self,id1,city):
        x = 1
        db = self.db
        cursor = db.cursor()
        cursor.execute('''select distinct user1.username from user1,friend1 where ((friend1.isFriend = 1 and friend1.id1 = ? and friend1.id2 = user1.id) or (friend1.isFriend = 1 and friend1.id2 = ? and friend1.id1 = user1.id)) and user1.city =?''', (id1,id1,city))
        while True:

            row = cursor.fetchone()  # lay ra 1 hang

            if row == None:
                break

            print(x,row[0])
            x=x+1













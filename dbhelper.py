import mysql.connector as connector
class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',port='3306',user='root',password='issue@11',database='pythontest')
        query='create table if not exists user(userId int primary key,userName varchar(200),bookIssued varchar(200))'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")


    #Insert
    def insert_user(self,userid,username,bookissued):
        query="insert into user(userId,userName,bookIssued) values({},'{}','{}')".format(userid,username,bookissued)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to database")
        return True


    #Fetch all
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("UserID : ",row[0])
            print("UserName : ",row[1])
            print("BookIssued : ",row[2])
            print()
            print()

    #Delete user
    def delete_user(self,userId):
        query="delete from user where userId= {}".format(userId)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("Deleted")

    #update
    def update_user(self,userId,newusername,newbookissued):
        query="Update user set userName = '{}', bookIssued = '{}' where userId = {} ".format(newusername,newbookissued,userId)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")

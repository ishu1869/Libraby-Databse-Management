from dbhelper import DBHelper

def main():
    db=DBHelper()
    while True:
        print("************** WELCOME *************")
        print()
        print("PRESS 1 to Insert new user")
        print("PRESS 2 to Disply all user")
        print("PRESS 3 to Delete user")
        print("PRESS 4 to Upadate user")
        print("PRESS 5 to exit program")
        print()
        try:
            choice=int(input())
            if(choice==1):
                #insert user
                uid = int(input("Enter user ID: "))
                username = (input("Enter user name: "))
                bookissued = (input("Enter Issued Book Name: "))
                db.insert_user(uid,username,bookissued)
                pass
            elif choice==2:
                #display user
                db.fetch_all()
                pass
            elif choice==3:
                #delete user
                userid=int(input("Enter user Id which you want to delete: "))
                db.delete_user(userid)
                pass
            elif choice==4:
                #upadate user
                uid = int(input("Enter user ID: "))
                username = (input("Enter new user name: "))
                bookissued = (input("Enter new Issued Book Name: "))
                db.update_user(uid,username,bookissued)
                pass
            elif choice==5:
                break
            else:
                print("Invalid Input! Try Again ")

        except Exception as e:
            print(e)
            print("Invalid Detail! Try Again")

if __name__ == "__main__":
    main()

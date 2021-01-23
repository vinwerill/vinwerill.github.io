# adb.py
import os
class DB():
    def __init__(self):
        self.conn = None
        self.cur = None
        self.title_side = '-'*12
        self.all = []
        self.form = '{:<8} {:17} {:^7} {:^7}'

    def __enter__(self):
        os.system('clear')
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        os.system('clear')
        self.close()
        return False

    def open(self):
        """ 開啟資料庫連線
        """
        if self.conn is None:
            import sqlite3
            self.conn = sqlite3.connect('library.db')
            self.cur = self.conn.cursor()
        return True

    def close(self):
        """ 關閉資料庫連線
        """
        if self.conn is not None:
            self.conn.close()
            self.conn = None
        return True

    

    def list_users(self):
        """ 使用者列表
        """
        self.cur.execute("SELECT * FROM USERS")
        all_rows = self.cur.fetchall()
        print(self.form.format('ID', '帳號', '年齡', '可藉閱量'))
        print('-'*50)
        for row in all_rows:
            print(self.form.format(*row))
        print()

    def check_if_examinee_existed(self, arg_account):
        """ 檢查使用者是否註冊
        """
        self.cur.execute("SELECT * FROM USERS WHERE NAME LIKE ?", (arg_account, ))
        info = self.cur.fetchall()
        if info == []:
            return False
        else:
            return True
    def insert_or_update_examinee(self, account_id):
        """ 增修使用者
        """
        self.cur.execute("SELECT ID FROM USERS")
        n = max(self.cur.fetchall())
        # print(n[0])
        age = int(input('age: '))
        self.cur.execute("INSERT INTO USERS VALUES(?,?,?,?)", (n[0]+1,account_id,age,20))
        self.conn.commit()
        
    def show_item(self, condition, f = '', j = 0):
        # print(condition)
        try:
            self.cur.execute(condition)
        except:
            self.cur.execute(condition,(f,))
        self.all = self.cur.fetchall()
        if j == 1 or j == -1:
            self.cur.execute("SELECT BOOK FROM BORROWED_BOOK")
            li = self.cur.fetchall()
            tli = [i[0] for i in li]
        num = 1
        for i in self.all:
            if len(i) == 2 and j != -1:
                print('{:10}{:20}'.format(i[0],i[1]))
                num += 1
            elif len(i) == 4 and j == 1 and i[3] not in tli:
                print(self.form.format(num, i[1],i[2],i[3]))
                num += 1
            elif j == -1:
                print(str(num)+'.',end = ' ')
                self.cur.execute("SELECT BNAME FROM BOOKS WHERE CODE LIKE ?", (i[1], ))
                ele = self.cur.fetchone()[0]
                print(ele)
                num += 1

    def search_book(self, st, account):
        f = '%'+input('查詢: ')+'%'
        if st == 1:
            al = "SELECT ID, BNAME, WRITER, CODE FROM BOOKS WHERE BNAME LIKE ?"
            self.cur.execute("SELECT ID FROM BOOKS WHERE BNAME LIKE ?",(f,))
        elif st == 2:
            al = "SELECT ID, BNAME, WRITER, CODE FROM BOOKS WHERE WRITER LIKE ?"
            self.cur.execute("SELECT ID FROM BOOKS WHERE WRITER LIKE ?",(f,))
        IDlist = self.cur.fetchall()
        print(self.form.format('編號', '名稱', '館藏量', '代碼'))
        self.show_item(al, f, 1)
        self.borrow_book(account, IDlist)
    
    def borrow_book(self, account, ID):
        n = input('輸入編號選擇書籍 q.返回: ')
        if n == 'q':
            pass
        elif n.isnumeric():
            self.cur.execute("SELECT BORROW_QUANTITY FROM USERS WHERE NAME LIKE ?",(account,))
            q = self.cur.fetchall()[0]
            # print(q)
            if q[0] == 0:
                print('已達到借閱書籍上限，請先歸還書籍以繼續動作')
            else:
                n = ID[int(n)][0]
                self.cur.execute("SELECT BNAME, CODE FROM BOOKS WHERE ID LIKE ?",(n,))
                book = self.cur.fetchall()[0]
                # print(account, book)
                self.cur.execute("INSERT INTO BORROWED_BOOK VALUES(?,?)", (account, book[1]))
        else:
            print('Error')
            self.borrow_book()
        self.conn.commit()

    def delete_book(self,):
        pass

    def return_book(self, code, account):
        self.cur.execute("SELECT BORROW_QUANTITY FROM USERS WHERE NAME LIKE ?",(account,))
        q = self.cur.fetchall()[0]
        self.cur.execute("UPDATE USERS SET BORROW_QUANTITY = ? WHERE NAME LIKE ?",(q+1, account,))
        
if __name__ == '__main__':
    print('This is the DB class.')
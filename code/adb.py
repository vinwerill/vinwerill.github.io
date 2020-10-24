# adb.py
class DB():
    def __init__(self):
        self.conn = None
        self.cur = None
        self.title_side = '-'*12
        self.all = []
        self.form = '{:<8} {:17} {:^7} {:^7}'

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
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
        
                        
    def print_examinee_info(self, account):
        """ 查詢使用者資訊
        """
        
    def show_item(self, condition, j = 1, f = ''):
        # print(condition)
        if j:
            self.cur.execute(condition)
        else:
            self.cur.execute(condition,(f,))
        self.all = self.cur.fetchall()
        for i in self.all:
            # print(i)
            if len(i) == 2:
                print('{:10}{:20}'.format(i[0],i[1]))
            elif len(i) == 4:
                print(self.form.format(i[0],i[1],i[2],i[3]))
    def search_book(self,st, account):
        f = '%'+input('查詢: ')+'%'
        if st == 1:
            al = "SELECT ID, BNAME, WRITER, STORE FROM BOOKS WHERE BNAME LIKE ?"
        elif st == 2:
            al = "SELECT ID, BNAME, WRITER, STORE FROM BOOKS WHERE WRITER LIKE ?"
        print(self.form.format('ID', '名稱', '館藏量', '已借閱量'))
        self.show_item(al, 0, f)
        self.borrow_book(account)
    
    def borrow_book(self, account):
        n = input('輸入編號選擇書籍 q.返回: ')
        if n == 'q':
            pass
        elif n.isnumeric():
            self.cur.execute("SELECT BORROW_QUANTITY FROM USERS WHERE NAME LIKE ?",(account,))
            q = self.cur.fetchall()[0]
            # print(q)
            if q[0] == 0:
                print('已達到借閱書籍上限，請先貴還書籍以繼續動作')
            else:
                n = int(n)
                self.cur.execute("SELECT BNAME, STORE FROM BOOKS WHERE ID LIKE ?",(n,))
                book = self.cur.fetchall()[0]
                print(account, book)
                if book[1] > 0:
                    self.cur.execute("INSERT INTO BORROWED_BOOK VALUES(?,?)",(account,book[0]))
                else:
                    print('該書已全部被借閱')
        else:
            print('Error')
            self.borrow_book()
        self.conn.commit()
    def delete_book(self,):
        pass
        
        
if __name__ == '__main__':
    print('This is the DB class.')
# auser.py
from adb import DB

# import sqlite3
# conn = sqlite3.connect('library.db')
# cur = conn.cursor()

class Examinee():
    def __init__(self):
        self.menu_title = '使用者'
        self.account = ''
        self.menu = {
            'l':'登入．註冊',
            'f':'書籍查詢',
            # 'c':'填充題測驗',
            'r':'歸還書籍',
            'c':'個人資料修改',
            # 'f':'推薦書籍',
            'q':'離開',
        }
        self.menu_func = {
            'l': lambda db, ft: self.login_or_signup(db, ft),
            'f': lambda db, ft: self.sear(db, self.account),
            # 'c': lambda db, ft: self.C(db, ft),
            'r': lambda db, ft: self.return_book(db),
            'c': lambda db, ft: self.F(db, ft),
            # 'f': lambda db, ft: self.G(db, ft),
        }
        self.divider = '='*20

    def show_menu(self, account=''):
        """ 主選單
        """
        print(self.divider)
        if self.account == '':
            print(self.menu_title, '尚未登入')
        else:
            print(self.menu_title, self.account)
            print('已借閱：')
            # db.show_item("SELECT * FROM BORROWED_BOOK WHERE USER LIKE ?", 0, self.account)
        print(self.divider)
        for fid, fname in self.menu.items():
            print('%s:%s' % (fid, fname))
        print(self.divider)
        opt = input('請選擇: ').lower()
        if opt in self.menu.keys():
            return opt, self.menu[opt]
        else:
            return '', '無此功能！'

    def login_or_signup(self, db, func_title):
        """ 登入．註冊
        """
        account_input = input('請輸入帳號: ')
        if db.check_if_examinee_existed(account_input):
            self.account = account_input
            db.print_examinee_info(self.account)
        else:
            db.insert_or_update_examinee(account_input)
            print()

    def sear(self, word_def, account):
        st =int(input("1.書名 2.作者: "))
        db.search_book(st, account)
        

    def P(self, db):
      pass

    def C(self, db, func_title):
        pass
            
    def return_book(self, db):
        db.show_item("SELECT * FROM BORROWED_BOOK WHERE USER LIKE ?", 0, self.account)
        n = input('輸入編號選擇書籍 q.返回: ')
        if n == 'q':
            pass
        elif n.isnumeric():
            pass

    def F(self, db, func_title):
        pass

    def G(self, db, func_title):
        pass

# entry point
with DB() as db:
    auser = Examinee()
    while True:
        func_id, func_name = auser.show_menu()
        if func_id == 'q':
            break
        elif func_id == '':
            print(func_name)
        else:
            if auser.account == '':
                func_id = 'l'
            auser.menu_func[func_id](db, func_name)
        print()
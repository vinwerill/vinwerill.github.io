# atestcenter.py
from adb import DB

# import sqlite3
# conn = sqlite3.connect('library.db')
# cur = conn.cursor()

class Center():
    def __init__(self):
        self.menu_title = '測驗中心'
        self.menu = {
            'a':'查閱書庫',
            'b':'館藏書籍設定',
            # 'c':'填充題型設定',
            'd':'使用者列表',
            'e':'借閱統計',
            # 'f':'個人成績查詢',
            'q':'離開',
        }
        self.menu_func = {
            'a': lambda db, ft: self.search_book(db, ft),
            'b': lambda db, ft: self.set_books(db, ft),
            # 'c': lambda db, ft: self.C(db, ft),
            'd': lambda db, ft: self.D(db, ft),
            'e': lambda db, ft: self.E(db, ft),
            # 'f': lambda db, ft: self.F(db, ft),
        }
        self.divider = '='*20

    def show_menu(self):
        """ 主選單
        """
        print(self.divider)
        print(self.menu_title)
        print(self.divider)
        for fid, fname in self.menu.items():
            print('%s:%s' % (fid, fname))
        print(self.divider)
        opt = input('請選擇: ').lower()
        if opt in self.menu.keys():
            return opt, self.menu[opt]
        else:
            return '', '無此功能！'

    def search_book(self, db, func_title):
        db.show_books("SELECT * FROM BOOKS")

    def set_books(self, db):
        n = int(input('1.新增 2.刪除 3.查詢 4.列表'))
        if n == 1:
            pass
        if n == 2:
            pass
        if n == 3:
            pass
        if n == 4:
            pass
        else:
            print('Error')
        

    def C(self, db, func_title):
       pass

    def D(self, db, func_title):
        db.list_users()

    def E(self, db, func_title):
        pass

    def F(self, db, func_title):
       pass

# entry point
with DB() as db:
    atestcenter = Center()
    while True:
        func_id, func_name = atestcenter.show_menu()
        if func_id == 'q':
            break
        elif func_id == '':
            print(func_name)
        else:
            atestcenter.menu_func[func_id](db, func_name)
        print()
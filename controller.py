# 扮演 controller 的角色
from view import InputView, OutputView, MenuView
from model import Product
from dao import Dao


class Controller:
    def __init__(self):
        self.__iv = InputView()
        self.__ov = OutputView()
        self.__mv = MenuView()
        self.__p = Product()
        self.__dao = Dao()

    def execute(self):
        one_data = self.__iv.enter_info()
        self.__p.set_product(one_data[0], one_data[1], one_data[2], one_data[3], one_data[4])
        self.__dao.connect_db()
        self.__dao.add_data(self.__p)
        self.__dao.disconnect_db()

    def search_alldb(self):
        self.__dao.connect_db()
        user_list = self.__dao.search_all()
        self.__ov.show_all(user_list)
        self.__dao.disconnect_db()

    def search_id_db(self):
        id＿ = self.__iv.enter_id_search()
        self.__dao.connect_db()
        u = self.__dao.search_id(id＿)
        self.__dao.disconnect_db()
        not_empty = self.__ov.show_id_search(u)
        return not_empty

    def delete_alldb(self):
        if self.__iv.enter_delete_alldb():
            self.__dao.connect_db()
            confirm_ = self.__dao.delete_all()
            self.__dao.disconnect_db()
            if confirm_:
                self.__ov.show_delete_alldb(confirm_)
            else:
                self.__ov.show_delete_alldb(confirm_)
        else:
            self.__ov.show_cancel_delete()

    def delete_id_db(self):
        num_ = self.__iv.enter_delete_id()
        self.__dao.connect_db()
        confirm_ = self.__dao.delete_id(num_)
        self.__dao.disconnect_db()
        self.__ov.show_delete_id(confirm_)

    def update_id_db(self):
        not_empty = self.search_id_db()
        if not_empty:
            one_data = self.__iv.enter_update_id()
            self.__dao.connect_db()
            confirm_ = self.__dao.update_id(one_data)
            self.__dao.disconnect_db()
            self.__ov.show_update_id(confirm_)
        else:
            return

    def run_menu(self):
        while True:
            self.__mv.nav()
            if self.__mv.choice == self.__mv.choose_execute:
                self.execute()
            elif self.__mv.choice == self.__mv.choose_search_alldb:
                self.search_alldb()
            elif self.__mv.choice == self.__mv.choose_search_id:
                self.search_id_db()
            elif self.__mv.choice == self.__mv.choose_delete_alldb:
                self.delete_alldb()
            elif self.__mv.choice == self.__mv.choose_delete_id:
                self.delete_id_db()
            elif self.__mv.choice == self.__mv.choose_update_id:
                self.update_id_db()
            elif self.__mv.choice == self.__mv.choose_end:
                break
        print('--- end ---')

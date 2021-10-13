from model import Product


class InputView:
    def enter_info(self):
        print('[InputView]')
        id_ = int(input('Product ID: '))
        name_ = input('Name: ')
        price_ = float(input('Price: '))
        quantity_ = int(input("Quantity: "))
        date_ = input('Date Added: ')
        return id_, name_, price_, quantity_, date_

    def enter_id_search(self):
        id_ = int(input('[InputView]\nSearch ID number: '))
        return id_

    def enter_delete_alldb(self):
        while True:
            d = input('Delete ALL data in db?(y/n)\n')
            if d.lower() == 'y':
                return True
            elif d.lower() == 'n':
                return False
            else:
                print('[error] Number invalid..')

    def enter_delete_id(self):
        num_ = int(input('[InputView]\nEnter ID (to be deleted): '))
        return num_

    def enter_update_id(self):
        print('[InputView]')
        id_ = int(input('Product ID(to be updated): '))
        price_ = float(input('Update Price (BLANK if unchanged): '))
        quantity_ = int(input('Update Quantity (BLANK if unchanged): '))
        return id_, price_, quantity_


class OutputView:
    def show_all(self, product_list: list):
        for product in product_list:
            p_ = Product(product[0], product[1], product[2], product[3], product[4])
            print(p_)

    def show_id_search(self, product_list: list):
        print('[OutputView] Id search..')
        if product_list:
            p_ = Product(product_list[0][0], product_list[0][1], product_list[0][2], product_list[0][3],
                         product_list[0][4])
            print(p_)
            return True
        else:
            print('No Match..')
            return False

    def show_delete_alldb(self, confirm_):
        print('[OutputView] Delete all in db..')
        if confirm_:
            print("Successful..")
        else:
            print("Delete failed (nothing in db)..")

    def show_cancel_delete(self):
        print('[OutputView]')
        print('Delete cancelled')

    def show_delete_id(self, confirm_):
        print('[OutputView] Delete id in db..')
        if confirm_:
            print("Delete successful..")
        else:
            print("Id not in db..")

    def show_update_id(self, confirm_):
        print('[OutputView] Update id in db..')
        if confirm_:
            print("Update successful..")
        else:
            print("Update unsuccessful(no input values)")


class MenuView:
    def __init__(self):
        self.choice = None
        self.choose_execute = 1
        self.choose_search_alldb = 2
        self.choose_search_id = 3
        self.choose_delete_alldb = 4
        self.choose_delete_id = 5
        self.choose_update_id = 6
        self.choose_end = 9

    def nav(self):
        s = '''\n[ShopMenu]
⑴  Add New 
⑵  Return Everything
⑶  Search by ID
⑷  Delete Everything 
⑸  Delete by ID
⑹  Update Price, Quantity
⑼  Exit
➤➤ '''
        self.choice = int(input(s))

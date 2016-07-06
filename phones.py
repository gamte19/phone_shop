from goods import Goods
import csv


class Phones(Goods):
    def __init__(self, *args):
        super().__init__(*args)

    @classmethod
    def get_csv(cls):
        phones_list = []
        with open("data/phones.csv", "r") as f:
            reader = csv.reader(f, delimiter=",")
            for phone in reader:
                phones_list.append(Phones(phone[0], phone[1], phone[2], int(phone[3]), int(phone[4])))
        return phones_list

    @classmethod
    def item_of_iphone(cls):
        x = cls.get_csv()
        iphone = 0
        samsung = 0
        for i in x:
            if i.product_name == "iphone":
                iphone += int(i.item)
            elif i.product_name == "samsung":
                samsung += int(i.item)
        return print("There are " + str(iphone) + " Iphone and " + str(samsung) + " samsung phone in the shop ")

    @classmethod
    def all_price_by_type(cls):
        x = cls.get_csv()
        phone_type_price = []
        keys = []
        values = []
        for i in x:
            temp_list = [i.product_name, i.product_type]
            temp_list = " ".join(temp_list)
            keys.append(temp_list)
            values.append(int(i.price) * int(i.item))
        dictionary = dict(zip(keys, values))
        print(dictionary)

    @classmethod
    def new_phone_arrived(cls):
        x = cls.get_csv()
        product_id = 11
        product_name = input("product name  ")
        product_type = input("product type  ")
        price = int(input("price  "))
        item = int(input("item  "))
        phone = [product_id, product_name, product_type, price, item]
        temp_list = []
        for i in x:
            temp_list.append(i)
        for i in x:
            if product_name == i.product_name and product_type == i.product_type:
                    i.item += item
            else:
                x.append(phone)



        for i in x:
            print(i.product_id, i.product_name, i.product_type, i.price, i.item)



x = Phones.get_csv()
for i in x:
    print(i.product_id, i.product_name, i.product_type, i.price, i.item)
Phones.item_of_iphone()
Phones.all_price_by_type()
Phones.new_phone_arrived()

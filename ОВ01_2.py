class Store():
    def __init__(self, name, address):
        self.name=name
        self.address=address
        self.assortment={}

    def add_product(self, product, price):
        self.assortment[product] = price

    def del_product(self,product):
        self.assortment.pop(product)
        print(f"{product} удалены из ассортимента")

    def new_price(self,product,price):
        self.assortment.update({product:price})
        print(f"{product}: новая цена - {price} руб.")

    def show_price(self,product):
        print(f"{product}: {self.assortment.get(product)} руб.")

    def show_assortment(self):
        print(f"Магазин: {self.name} - {self.address}")
        print("Ассортимент:")
        for key,value in self.assortment.items():
            print(f"{key} {value} руб.")


#вводим данные магазинов
st1=Store("Фрути", "Красная гора, 5")
st2=Store("Фрукты из Грузии", "Кикабидзе, 15")
st3=Store("Сладкий персик", "Кима, 7")

#Наименования товара
prod1="Яблоки"
prod2="Груши"
prod3="Сливы"
prod4="Вишни"

#добавление товара в магазин №2
st2.add_product(prod1,300)
st2.add_product(prod2,400)
st2.add_product(prod3,350)
st2.add_product(prod4,450)

#ассортимент товаров магазина №2
st2.show_assortment()

#обновление цены товара в магазине №2
st2.new_price("Груши",800)

#удаление товара из ассортимента магазина №2
st2.del_product("Сливы")

#запрос цены товара магазина №2
st2.show_price("Персики")
st2.show_price("Груши")









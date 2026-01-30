class Restaurant:
    dishes = {}
    orders = {}

    coupon_codes = {
        "STUDENT10": 0.10,
        "FAMILY20": 0.20,
    }
    def __init__(self):
        pass
    # Add dish
    def add_dish(self,name, price, category):
        dish = {
            "name": name,
            "price": price,
            "category": category
        }
        if price >= 0:
            self.dishes[name] = dish
        else:
            print('Dish price cannot be less than or equal to zero')


#Remove dish from list
    def remove_dish(self, name, category):
        for key in list(self.dishes.keys()):
        
            if self.dishes[key]['name'] == name and self.dishes[key]['category']==category:
                del self.dishes[key]
            else:
                print(f"Element with name {name} in the category {category} is not found!")
        print(f"{name} has been removed from the list")


#Print all items in the list
    def check_dishes(self):
        for key, values in self.dishes.items():
            print(f"{key}:{values}")

#ORDER MANAGEMENT
    def create_order(self, table_number):
        # Initialize an order with empty items and quantity 0
        self.orders[table_number] = {'id': table_number, 'items': []}
        return self.orders[table_number]

    # Add to orders
    def add_to_order(self, order_id, dish, qty):
        if order_id in self.orders:
            found = False
            for k, v in self.dishes.items():
                if v['name'] == dish:
                    item = {
                        'name': v['name'],
                        'price': v['price'],
                        'category': v['category'],
                        'quantity': qty
                    }

                    if item not in self.orders[order_id]['items']:
                        self.orders[order_id]['items'].append(item)
                        found = True
                        break
                    else:
                        for i in self.orders[order_id]['items']:
                            if i['name'] == dish:
                                i['quantity'] += qty
                        # self.orders[order_id]['items']['quantity'] += qty
                        found = True
                        break
            if not found:
                print("The dish not on the menu")
        else:
            print("Order ID does not exist")
        
        #calculate total
        total = 0
        for  item in self.orders[order_id]['items']:
            total += item['price'] * item['quantity']
        self.orders[order_id]['total'] = f"{total:.2f}" 
            
    def check_orders(self):
        # for key, values in self.orders.items():
        #     print("The orders are:")
        #     print(f"{key}:{values}")
        print(self.orders)

    # Apply discount with coupon code

    def apply_discount(self,order_id, code):
        if code not in self.coupon_codes:
            print("This discount code does not exist")
        
        for k,order in self.orders.items():
            rate = self.coupon_codes[code]
            
            if k == order_id:
                total = float(order['total'])
                discount_amount  = total * rate
                new_total = total - discount_amount

                self.orders[order_id]['total'] = f"{new_total:.2f}"

    
    def get_table_bill(self,order_id):
        if order_id not in self.orders:
            raise ValueError("Order ID does not exist")
        bill = 0
        for k,order in self.orders.items():
            if order['id'] ==  order_id:
                bill= bill + float(order['total']) 
        return f"{bill:.2f}"



restau = Restaurant()

restau.add_dish("Pizza",20, "main")
restau.add_dish("Salad", 8.99, "appetizer")
restau.add_dish("Orange", 2.99, "Drink")
restau.add_dish("Cola", 2.99, "Drink")


restau.check_dishes()

# restau.remove_dish('Pizza','main')
print("new list")

restau.check_dishes()

order_id = restau.create_order(1)
order_id = restau.create_order(2)
print(order_id)

restau.add_to_order(2,'Salad',2)
restau.add_to_order(2,'Pizza',2)
restau.add_to_order(2,'Salad',2)
restau.add_to_order(2,'Orange',4)
restau.add_to_order(1,'Salad',2)
restau.add_to_order(1,'Orange',4)
restau.check_orders()

restau.apply_discount(2,"STUDENT10")
restau.check_orders()


bill = restau.get_table_bill(2)
print(f"The total bill for table 2 is: ${bill}")
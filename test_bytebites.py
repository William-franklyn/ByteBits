from models import MenuItem, Customer, MenuCollection, Transaction
def  test_menu_item():
    item = MenuItem(name="Burger", price=5.99, category="Main")
    assert item.name == "Burger"
    assert item.price == 5.99
    assert item.category == "Main"

def test_customer():
    customer = Customer(name="Alice")
    assert customer.name == "Alice"
    assert customer.purchase_history == []
    assert not customer.is_verified()
    
def test_menu_collection():
    menu = MenuCollection()
    item1 = MenuItem(name="Burger", price=5.99, category="Main")
    item2 = MenuItem(name="Fries", price=2.99, category="Side")
    menu.add_item(item1)
    menu.add_item(item2)
    
    assert len(menu.items) == 2
    assert menu.find_item("Burger") == item1
    assert menu.filter_by_category("Side") == [item2]   
    assert menu.remove_item("Burger") == True
    assert menu.find_item("Burger") == None            
def test_transaction():
    customer = Customer(name="Bob")
    transaction = Transaction(customer=customer)
    item1 = MenuItem(name="Pizza", price=8.99, category="Main")
    item2 = MenuItem(name="Soda", price=1.99, category="Drink")
    
    transaction.add_item(item1)
    transaction.add_item(item2)
    
    assert transaction.total_cost() == 10.98
    assert transaction.item_names() == ["Pizza", "Soda"]
    
    transaction.commit()
    assert len(customer.purchase_history) == 1
    assert customer.is_verified()                                                   




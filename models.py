# Models for the ByteBites app with classes for User, MenuItem, MenuCollection, and Transaction .

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class MenuItem:
    name: str
    price: float
    category: str
    popularity_rating: float = 0.0

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("price must be >= 0")
        if not (0 <= self.popularity_rating <= 5):
            raise ValueError("popularity_rating must be between 0 and 5")

    def __str__(self):
        return f"{self.name} (${self.price:.2f}) [{self.category}] rating={self.popularity_rating}" 


@dataclass
class Customer:
    name: str
    purchase_history: List[Transaction] = field(default_factory=list)

    def add_transaction(self, transaction: Transaction) -> None:
        self.purchase_history.append(transaction)

    def total_spent(self) -> float:
        return sum(tx.total_cost() for tx in self.purchase_history)

    def is_verified(self) -> bool:
        return len(self.purchase_history) > 0


@dataclass
class MenuCollection:
    items: List[MenuItem] = field(default_factory=list)

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def remove_item(self, item_name: str) -> bool:
        for i, item in enumerate(self.items):
            if item.name == item_name:
                self.items.pop(i)
                return True
        return False

    def filter_by_category(self, category: str) -> List[MenuItem]:
        return [item for item in self.items if item.category.lower() == category.lower()]

    def find_item(self, item_name: str) -> MenuItem | None:
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None


@dataclass
class Transaction:
    customer: Customer
    items: List[MenuItem] = field(default_factory=list)

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def total_cost(self) -> float:
        return sum(item.price for item in self.items)

    def item_names(self) -> List[str]:
        return [item.name for item in self.items]

    def commit(self) -> None:
        # Add to customer history
        self.customer.add_transaction(self)

    def __str__(self):
        names = ', '.join(self.item_names())
        return f"Transaction(customer={self.customer.name}, items=[{names}], total={self.total_cost():.2f})"


if __name__ == '__main__':
    # Example usage
    menu = MenuCollection()
    menu.add_item(MenuItem(name='Spicy Burger', price=8.99, category='Food', popularity_rating=4.8))
    menu.add_item(MenuItem(name='Large Soda', price=2.99, category='Drinks', popularity_rating=4.2))
    menu.add_item(MenuItem(name='Chocolate Cake', price=5.49, category='Desserts', popularity_rating=4.9))

    drinks = menu.filter_by_category('Drinks')
    print('Drinks:', drinks)

    customer = Customer(name='Alice')
    tx = Transaction(customer=customer)
    tx.add_item(menu.find_item('Spicy Burger'))
    tx.add_item(menu.find_item('Large Soda'))
    print('Transaction total:', tx.total_cost())
    tx.commit()

    print('Customer verified:', customer.is_verified())
    print('Total spent by customer:', customer.total_spent())
 
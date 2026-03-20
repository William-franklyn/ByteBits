+-------------------+
|     MenuItem      |
+-------------------+
| - name: str       |
| - price: float    |
| - category: str   |
| - popularity_rating: float |
+-------------------+
| + __post_init__() |
| + __str__()       |
+-------------------+

+-------------------+
|      User         |
+-------------------+
| - name: str       |
| - purchase_history: List<Transaction> |
+-------------------+
| + add_transaction(tx) |
| + total_spent()       |
| + is_verified()       |
+-------------------+

+-----------------------+
|   MenuCollection      |
+-----------------------+
| - items: List<MenuItem> |
+-----------------------+
| + add_item(item)        |
| + remove_item(item_name)|
| + filter_by_category(c) |
| + find_item(item_name)  |
+-----------------------+

+-------------------+
|   Transaction     |
+-------------------+
| - customer: User  |
| - items: List<MenuItem> |
+-------------------+
| + add_item(item)      |
| + total_cost()        |
| + item_names()        |
| + commit()            |
| + __str__()          |
+-------------------+
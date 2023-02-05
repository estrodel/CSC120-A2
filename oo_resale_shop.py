from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory: Dict[int, Dict[str, Union[str, int, bool]]] = {}

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self)->None:
        pass
       
    def buy(self,computer: Dict[str, Union[str, int, bool]]):
        itemID = len(self.inventory)+1
        self.inventory[itemID] = computer
        return itemID

    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")



from Warehouse import Warehouse


class InventoryAllocator:
    """
    InventoryAllocator encapsulates a dictionary of strings and integers and a list of Warehouses.
    """
    def __init__(self, order, warehouses):
        """
        Construct a new 'InventoryAllocator' object.

        :param order: dictionary representing different types and quantities of items
        :param warehouses: list of warehouses where items are stored
        :return: returns nothing
        """
        self.order = order
        self.warehouses = warehouses

    def complete_order(self):
        """
        Calculates best method of shipping items in order.
        Function searches through each Warehouse in warehouses (which are in cost order),
        determines if any items from the order are in that Warehouse, and if they are, adds
        that Warehouse to the list of Warehouses being returned with the items and quantities it
        should ship.
        :return: List of Warehouses containing items they need to ship based on the order
        """
        ret = []
        # Loops through each Warehouse in warehouses
        for w in self.warehouses:
            shared_items = []
            # Loops through each item in the order
            for item in self.order.keys():
                # If there is an item in both the Warehouse and the order of a quantity greater than 0 for each
                # then it is added to the list of shared items
                if self.order[item] > 0 and item in w.inventory.keys() and w.inventory[item] > 0:
                    shared_items.append(item)
            # If there are any shared items between the order and the Warehouse
            if len(shared_items) > 0:
                # This is the Warehouse with shared items, however, it is undetermined how much of which item this
                # Warehouse will ship
                ret_w = Warehouse(w.name, {})
                # Loops over each shared item
                for item in shared_items:
                    # If there is more of this item (or an equal amount) in the Warehouse than in the order,
                    # the Warehouse should ship the amount remaining in the order
                    # and this item is removed from the order
                    if self.order[item] <= w.inventory[item]:
                        ret_w.inventory[item] = self.order[item]
                        self.order.pop(item)
                    # If there is more of this item in the order than in the Warehouse,
                    # the Warehouse should ship the entirety of its stock of this item
                    # and the quantity of this item in the order is decreased by the quantity possessed by the Warehouse
                    else:
                        ret_w.inventory[item] = w.inventory[item]
                        self.order[item] = self.order[item] - w.inventory[item]
                ret.append(ret_w)
        if len(self.order.keys()) > 0:
            return []
        return ret
from Warehouse import Warehouse


class InventoryAllocator:

    def __init__(self, order, warehouses):
        self.order = order
        self.warehouses = warehouses

    def complete_order(self):
        ret = []
        for w in self.warehouses:
            shared = []
            for item in self.order.keys():
                if self.order[item] > 0 and item in w.inventory.keys() and w.inventory[item] > 0:
                    shared.append(item)
            if len(shared) > 0:
                ret_w = Warehouse(w.name, {})
                for item in shared:
                    if self.order[item] <= w.inventory[item]:
                        ret_w.inventory[item] = self.order[item]
                        self.order.pop(item)
                    else:
                        ret_w.inventory[item] = w.inventory[item]
                        self.order[item] = self.order[item] - w.inventory[item]
                ret.append(ret_w)
        if len(self.order.keys()) > 0:
            return []
        return ret
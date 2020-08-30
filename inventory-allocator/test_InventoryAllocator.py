import unittest
from InventoryAllocator import InventoryAllocator
from Warehouse import Warehouse


class TestInventoryAllocator(unittest.TestCase):
    """
    test_InventoryAllocator is a Unit Test which tests functionality of the InventoryAllocator class
    """

    # tests when 1 warehouse perfectly matches a 1 item order
    def test_one(self):
        order = {'apple': 2}
        warehouses = [Warehouse('owd', {'apple': 2})]
        expected_value = [Warehouse('owd', {'apple': 2})]
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # tests when 2 warehouses perfectly split a 1 item order
    def test_two(self):
        order = {'apple': 10}
        warehouses = [Warehouse('owd', {'apple': 5}), Warehouse('dm', {'apple': 5})]
        expected_value = [Warehouse('owd', {'apple': 5}), Warehouse('dm', {'apple': 5})]
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # tests when only warehouse has 0 of a 1 item order
    def test_three(self):
        order = {'apple': 1}
        warehouses = [Warehouse('owd', {'apple': 0})]
        expected_value = []
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # tests when only warehouse does not have enough of a 1 item order
    def test_four(self):
        order = {'apple': 2}
        warehouses = [Warehouse('owd', {'apple': 1})]
        expected_value = []
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # tests when warehouses split 1 item order but not all of the inventory is needed
    def test_five(self):
        order = {'apple': 10}
        warehouses = [Warehouse('owd', {'apple': 8}), Warehouse('dm', {'apple': 5})]
        expected_value = [Warehouse('owd', {'apple': 8}), Warehouse('dm', {'apple': 2})]
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # tests when 2 warehouses perfectly split a 2 item order
    def test_six(self):
        order = {'apple': 10, 'banana': 10}
        warehouses = [Warehouse('owd', {'apple': 7, 'banana': 3}), Warehouse('dm', {'apple': 3, 'banana': 7})]
        expected_value = [Warehouse('owd', {'apple': 7, 'banana': 3}), Warehouse('dm', {'apple': 3, 'banana': 7})]
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # tests when 2 warehouses split a 2 item order but not all of the inventory is needed
    def test_seven(self):
        order = {'apple': 10, 'banana': 10}
        warehouses = [Warehouse('owd', {'apple': 9, 'banana': 8}), Warehouse('dm', {'apple': 3, 'banana': 7})]
        expected_value = [Warehouse('owd', {'apple': 9, 'banana': 8}), Warehouse('dm', {'apple': 1, 'banana': 2})]
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # tests when 2 warehouses split a 2 item order and there is not enough inventory for one of the items
    def test_eight(self):
        order = {'apple': 10, 'banana': 10}
        warehouses = [Warehouse('owd', {'apple': 9, 'banana': 8}), Warehouse('dm', {'apple': 3, 'banana': 1})]
        expected_value = []
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # tests when warehouses split a two item order but neither have every item in the order
    def test_nine(self):
        order = {'apple':15, 'banana': 15, 'cherry': 15}
        warehouses = [Warehouse('w1', {'apple':15, 'banana':7}), Warehouse('w2', {'banana':8, 'cherry':15})]
        expected_value = [Warehouse('w1', {'apple':15, 'banana':7}), Warehouse('w2', {'banana':8, 'cherry':15})]
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # tests when a Warehouse does not have an item from the order
    def test_ten(self):
        order = {'apple': 15, 'banana': 15}
        warehouses = [Warehouse('w1', {'apple': 15, 'cherry': 15})]
        expected_value = []
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # tests when a Warehouse has items not in the order
    def test_eleven(self):
        order = {'apple': 15, 'cherry': 15}
        warehouses = [Warehouse('w1', {'apple': 15, 'banana': 15, 'cherry': 15})]
        expected_value = [Warehouse('w1', {'apple': 15, 'cherry': 15})]
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # tests when warehouses split a two item order but both have items not in the order and not all the inventory is needed
    def test_twelve(self):
        order = {'apple': 15, 'banana': 15, 'cherry': 15}
        warehouses = [Warehouse('w1', {'apple': 100, 'banana': 14, 'duck':4}), Warehouse('w2', {'banana': 100, 'cherry': 100})]
        expected_value = [Warehouse('w1', {'apple': 15, 'banana': 14}), Warehouse('w2', {'banana': 1, 'cherry': 15})]
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # test when warehouses have items not in order and do not have an item in the order
    def test_thirteen(self):
        order = {'apple': 15, 'banana': 15, 'cherry': 15}
        warehouses = [Warehouse('w1', {'apple': 100, 'squash': 14, 'duck': 4}), Warehouse('w2', {'banana': 100, 'car': 100})]
        expected_value = []
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # test when warehouses and order are empty sets and maps respectively
    def test_fourteen(self):
        order = {}
        warehouses = []
        expected_value = []
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # tests when item in order is of quantity 0
    def test_fifteen(self):
        order = {'apple': 0}
        warehouses = [Warehouse('w1', {'apple': 100, 'banana': 19})]
        expected_value = []
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # test when order has items of quantity 0
    def test_sixteen(self):
        order = {'apple': 10, 'banana': 0}
        warehouses = [Warehouse('w1', {'apple': 100, 'banana': 19}),  Warehouse('w2', {'banana': 100, 'cherry': 100})]
        expected_value = []
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # test when warehouse's map and order map are in different orders
    def test_seventeen(self):
        order = {'apple': 100, 'banana': 200, 'cherry': 300}
        warehouses = [Warehouse('w1', {'cherry': 500, 'apple': 200, 'banana': 400})]
        expected_value = [Warehouse('w1', {'apple': 100, 'banana': 200, 'cherry': 300})]
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # tests when not every warehouse needs to ship items
    def test_eighteen(self):
        order = {'apple': 100, 'banana': 200, 'cherry': 300}
        warehouses = [Warehouse('w1', {'apple': 50, 'banana': 50, 'cherry': 50}),
                      Warehouse('w2', {'apple': 300, 'banana': 300, 'cherry': 300}),
                      Warehouse('w2', {'apple': 50, 'banana': 50, 'cherry': 50})]
        expected_value = [Warehouse('w1', {'apple': 50, 'banana': 50, 'cherry': 50}),
                          Warehouse('w2', {'apple': 50, 'banana': 150, 'cherry': 250})]
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

    # tests when there is a large order, many warehouses, extra items in the warehouses, and some extra inventory
    def test_nineteen(self):
        order = {'apple': 1000, 'banana': 1000, 'cherry': 1000, 'duck': 1000, 'eggs': 10000}
        warehouses = [Warehouse('w1', {'car': 500, 'apple': 100}),
                      Warehouse('w2', {'banana':1000, 'duck': 500, 'cherry':800}),
                      Warehouse('w3', {'apple': 900, 'banana': 1999, 'turkey': 100000, 'eggs':5000}),
                      Warehouse('w4', {'cherry': 250}),
                      Warehouse('w5', {'chicken': 5500, 'duck': 1000, 'apple': 14, 'ketchup': 16}),
                      Warehouse ('w6', {'eggs': 5500, 'banana': 5, 'cherry': 100, 'chicken': 8})]
        expected_value = [Warehouse('w1', {'apple': 100}),
                          Warehouse('w2', {'banana': 1000, 'cherry': 800, 'duck': 500}),
                          Warehouse('w3', {'apple': 900, 'eggs': 5000}),
                          Warehouse('w4', {'cherry': 200}),
                          Warehouse('w5', {'duck': 500}),
                          Warehouse('w6', {'eggs': 5000})]
        result = InventoryAllocator(order, warehouses).complete_order()
        self.assertEqual(expected_value, result)

if __name__ == '__main__':
    unittest.main()

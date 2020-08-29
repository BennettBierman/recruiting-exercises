class Warehouse:
    """
       Warehouse encapsulates a string and a dictionary of strings and integers.
       """
    def __init__(self, name, inventory):
        """
        Construct a new 'Warehouse' object.

        :param name: string representing name of Warehouse
        :param inventory: dictionary representing names and quantities of items stored in Warehouse
        :return: returns nothing
        """
        self.name = name
        self.inventory = inventory

    def __str__(self):
        """
        Construct string to represent state of a Warehouse object.

        :return: returns a string
        """
        return f"{{name: {self.name}, inventory: {self.inventory}}}"

    def __repr__(self):
        """
        Construct string to represent state of a Warehouse object.

        :return: returns a string
        """
        return f"{{name: {self.name}, inventory: {self.inventory}}}"

    def __eq__(self, other):
        """
        Determine equality between this Warehouse and another Warehouse object.
        Warehouses are equal if their string and dictionary are equal

        :param other: another Warehouse object
        :return: returns boolean representing whether two objects are equal
        """
        return self.name == other.name and self.inventory == other.inventory

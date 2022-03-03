class Menu():
    def __init__(self, items):
        self.items = items
    
    def precio(self, dict_items):
        precio = 0
        for nombre_item in dict_items.keys():
            precio += self.items[nombre_item] * dict_items[nombre_item]
        return precio
    
    def tamaño(self):
        return len(self.items)


mi_menu = Menu({'latte':25, 'medialuna':15})

print(mi_menu.precio({'latte': 10, 'medialuna':30}))






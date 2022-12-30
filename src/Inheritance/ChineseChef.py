from Chef import Chef

# class ChineseChef inherits class Chef
class ChineseChef(Chef):    

    # Overrided from Chef class
    def make_special_dish(self):
        print("The chef makes orange chicken")
    
    def make_fried_rice(self):
        print("The chef makes fried rice")
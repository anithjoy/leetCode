class Machine:
    def __init__(self, Type, Name, Speed):
        self.Type = Type
        self.Name = Name
        self.Speed = Speed

    def __str__(self):
        return (f"{self.Name} is a {self.Type}")
    

class Car(Machine):
    def __init__(self, Type, Name, Speed, Owner):
        Machine.__init__(self, Type, Name, Speed)
        self.Owner = Owner

    def __str__(self):
        return (f"{self.Name} is a {self.Type} of Owner {self.Owner}")
    

    def start(self):
        print(f"{self.Type} {self.Name} started of Owner {self.Owner}")
        self.helper()

    def stop(self):
        print(f"{self.Type} {self.Name} stopped of Owner {self.Owner}")

    def helper(self):
        print("This is a helper function")
    
    
        

    




if __name__ == '__main__':
    print("Running")
    mercedes = Machine("Car", "Mercedes", 35)

    # car class
    baleno = Car("Car","Baleno", 40, "Manya")
    print(baleno)
    baleno.start()
    baleno.stop()
    


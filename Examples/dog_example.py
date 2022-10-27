class Dog:
    counter = 0
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Dog.counter += 1
    def bark(self, times):
        for i in range(times):
            if self.weight > 10:
                print(f"Wuf wuff!! Olen iso {self.name}")
            else:
                print(f"wuf wuf! Olen pieni {self.name}")



dog1 = Dog("Rekku", 8)
dog2 = Dog("Ruffe", 12)
dog1.bark(3)
dog2.bark(1)
dog3 = Dog("Aku", 5)
print("Koiria yhteensä", Dog.counter)
#print("Koira 1:", dog1.name, dog1.weight, "kg")
#print("Koira 2", dog2.name, dog2.weight, "kg")
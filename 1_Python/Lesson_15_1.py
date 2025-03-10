class Transport:

   def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage
   
   def Autobus(self):
       print(f'Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}')

t1 = Transport('Renaul Logan', 180, 12)

t1.Autobus()
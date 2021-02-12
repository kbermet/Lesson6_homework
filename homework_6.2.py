# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при созании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого дляпокрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия
# одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def formula(self):
        return (self._length*self._width*25*5)/1000

my_road = Road(5000, 20)
print(my_road.formula())
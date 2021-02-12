# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “апуск отрисовки.” Создать ри доерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title = "Drawing tool"):
        self.title = title

    def draw(self):
        print(f'Draw with {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Draw with {self.title} pen')

class Pencil(Stationery):
    def draw(self):
        print(f'Draw with {self.title} pencil')

class Marker(Stationery):
    def draw(self):
        print(f'Draw with {self.title} marker')


stat = Stationery()
stat.draw()
pen=Pen('ABC')
pen.draw()
pencil=Pencil('Pony')
pencil.draw()
marker=Marker('XYZ')
marker.draw()
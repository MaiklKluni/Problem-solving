    # Задача 1. 5 подъездов, 20 квартир (100 квартир, 5 этажей) -
    # определить этаж и подъезд по номеру квартиры
def task_1():
    number_house = int(input('Введите число от одного до ста: '))
    number_door = number_house // 21 + 1
    number_href = number_house // (number_door * 5) + 1
    print(f'Номер подъезда: {number_door}\nЭтаж: {number_href}')

if __name__ == "__main__":
    task_1()



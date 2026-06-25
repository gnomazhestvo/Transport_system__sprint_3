"""
Финальный проект Спринта 3 - основы ООП.

Система управления транспортными средствами.
"""


def validate_fuel_consumption(method):
    """
    Декоратор для проверки условий перед расчётом расхода топлива.

    Проверяет, что время или расстояние неотрицательны и достаточно топлива.
    """
    def wrapper(self, value):
        if value is None:
            # Если метод вернул None, также возвращает None.
            return

        elif value < 0:
            print('Ошибка: значение не может быть отрицательным.')
            return

        else:
            result = method(self, value)  # Вычисляем расход.
            if result > self._current_fuel_level:
                # Если топлива недостаточно для путешествия, то ошибка.
                print(
                    f'Ошибка: недостаточно топлива для поездки. '
                    f'Нужно {result} л, в наличии {self._current_fuel_level} л."'
                )
                return
            else:
                # Если все проверки пройдены, то вычитает расход из текущего
                # уровня топлива и возвращает расход.
                self._current_fuel_level -= result
        return result
    return wrapper


class Vehicle:
    """Базовый класс для транспортных средств."""

    def __init__(self, name, fuel_tank_capacity):
        """Инициализация атрибутов."""
        self._name = name
        self._fuel_tank_capacity = fuel_tank_capacity
        self._current_fuel_level = fuel_tank_capacity

    def refuel(self, amount):
        """Заправка транспортного средства на указанное кол-во топлива."""
        if amount <= 0:
            print('Ошибка: количество топлива должно быть положительным.')
            return

        elif (amount + self._current_fuel_level) > self._fuel_tank_capacity:
            print('Ошибка: превышение вместимости топливного бака.')
            return
    
        elif amount > 0 and (amount + self._current_fuel_level) <= self._fuel_tank_capacity:
            self._current_fuel_level += amount
            print(
                f'Заправлено {amount} л. '
                f'Текущий уровень: {self._current_fuel_level} л.'
            )

    def display_info(self):
        """Отображает основную информацию о транспортном средстве."""
        print(
            f'Название: {self._name}, '
            f'Вместимость бака: {self._fuel_tank_capacity} л, '
            f'Текущий уровень топлива: {self._current_fuel_level} л.'
        )


class Car(Vehicle):
    """
    Класс для представления автомобиля.

    Наследует от Vehicle.
    """

    def __init__(self, name, fuel_tank_capacity, fuel_consumption_per_100km):
        """Инициализация атрибутов."""
        super().__init__(name, fuel_tank_capacity)
        self._fuel_consumption_per_100km = fuel_consumption_per_100km

    @validate_fuel_consumption
    def calculate_fuel_consumption(self, distance):
        """Рассчитывает расход топлива для поездкии на заданное расстояние."""
        consumption = round((distance / 100) * self._fuel_consumption_per_100km, 2)
        print(f'Расход на {distance} км: {consumption} л.')
        return consumption


class Airplane(Vehicle):
    """
    Класс для представления самолёта.

    Наследует от Vehicle.
    """

    def __init__(self, name, fuel_tank_capacity, fuel_consumption_per_hour):
        """Инициализация атрибутов."""
        super().__init__(name, fuel_tank_capacity)
        self._fuel_consumption_per_hour = fuel_consumption_per_hour

    @validate_fuel_consumption
    def calculate_fuel_consumption(self, flight_time):
        """Рассчитывает расход топлива для полета на заданное время."""
        consumption = round(flight_time * self._fuel_consumption_per_hour, 2)
        print(f'Расход за {flight_time} ч: {consumption} л.')
        return consumption


class Boat(Vehicle):
    """
    Класс для представления катера.

    Наследует от Vehicle.
    """

    def __init__(self, name, fuel_tank_capacity, fuel_consumption_per_hour):
        """Инициализация атрибутов."""
        super().__init__(name, fuel_tank_capacity)
        self._fuel_consumption_per_hour = fuel_consumption_per_hour

    @validate_fuel_consumption
    def calculate_fuel_consumption(self, travel_time):
        """Рассчитывает расход топлива для заплыва на заданное время."""
        consumption = round(travel_time * self._fuel_consumption_per_hour, 2)
        print(f'Расход за {travel_time} ч: {consumption} л.')
        return consumption


# Создание объектов
car = Car("Toyota Camry", 60, 8)
airplane = Airplane("Boeing 737", 20000, 2500)
boat = Boat("Sea Ray", 150, 30)

# Отображение информации
# Название: Toyota Camry, Вместимость бака: 60 л, Тек. уровень топлива: 60 л.
car.display_info()

# Название: Boeing 737, Вместимость бака: 20000 л, Текущий уровень
# топлива: 20000 л.
airplane.display_info()

# Название: Sea Ray, Вместимость бака: 150 л, Текущий уровень топлива: 150 л.
boat.display_info()


# Заправка транспортных средств
car.refuel(30)  # Ошибка: превышение вместимости топливного бака.
airplane.refuel(10000)  # Ошибка: превышение вместимости топливного бака.
boat.refuel(80)  # Ошибка: превышение вместимости топливного бака.


# Расчёт расхода топлива
# Расход на 1500 км: 120.00 л. Ошибка: недостаточная вместительность бака.
car.calculate_fuel_consumption(1500)
airplane.calculate_fuel_consumption(3)  # Расход за 3 ч: 7500.00 л.
boat.calculate_fuel_consumption(-1)  # Значение не может быть отрицательным.
boat.calculate_fuel_consumption(None)  # Расход за 2 ч: 60.00 л.
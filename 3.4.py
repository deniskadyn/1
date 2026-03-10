class Car:
    wheels: int = 4
    has_engine: bool = True

    def __init__(self, brand: str, model: str, year: int, color: str, fuel: str) -> None:
        self.brand: str = brand
        self.model: str = model
        self.year: int = year
        self.color: str = color
        self.fuel: str = fuel
        self.is_running: bool = False  # Заведен ли двигатель

    """
    Инициализация объекта автомобиля.
    Args:
        brand: Марка автомобиля
        model: Модель автомобиля
        year: Год выпуска
        color: Цвет автомобиля
        fuel: Тип топлива (бензин, дизель, электричество)
    """

    def __str__(self) -> str:
        return f"{self.color} {self.brand} {self.model}, {self.year} года, Топливо: {self.fuel}"

    def start(self, key: str) -> str:
        if key.lower() == "зажигание":
            self.is_running = True
            return f"{self.brand} {self.model} завелся! Двигатель работает"
        else:
            return f"{self.brand} {self.model} не завелся, нужен ключ зажигания"

    def drive(self, km: int) -> str:
        if km < 10:
            return f"{self.brand} {self.model} проехал {km} км, это короткая поездка"
        elif km > 500:
            return f"{self.brand} {self.model} проехал {km} км, это очень далеко, нужна заправка"
        else:
            return f"{self.brand} {self.model} проехал {km} км, хорошая поездка"

    def stop(self) -> str:
        self.is_running = False
        return f"{self.brand} {self.model} заглушил двигатель"

    def refuel(self, liters: int) -> None:
        if liters > 0:
            print(f"{self.brand} {self.model} заправили {liters} литров {self.fuel}")


car1 = Car("Toyota", "Camry", 2022, "серебристый", "бензин")
car2 = Car("Tesla", "Model S", 2023, "красный", "электричество")
car3 = Car("BMW", "X5", 2021, "черный", "дизель")

print(car1)
print(car2)
print(car3)

print(f"Колес у машин: {Car.wheels}")
print(f"Есть двигатель: {Car.has_engine}")

print(car2.start("зажигание"))
car1.drive(250)
car3.drive(600)
car1.stop()
car2.refuel(50)
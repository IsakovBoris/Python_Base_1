class Worker:


    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.position = position
        self._income = income


class Position(Worker):


    def get_full_name(self) -> str:
        """Возвращает строку по формату 'Имя Фамилия'"""
        return f'{self.name} {self.surname}'


    def get_total_income(self) -> int:
        result = 0
        for sallary in self._income.values():
            result += sallary
        return result



if __name__ == '__main__':
    welder = Position('иван', 'васильев', 'сварщик', {'wage': 50000, 'bonus': 15000})
    driver = Position('петр', 'николаев', 'водитель', {'wage': 30000, 'bonus': 7500})
    scientist = Position('геннадий', 'разумов', 'ученый', {'wage': 150000, 'bonus': 25000})
    print(welder.get_full_name(), welder.get_total_income())
    print(driver.get_full_name(), driver.get_total_income())
    print(scientist.get_full_name(), scientist.get_total_income())

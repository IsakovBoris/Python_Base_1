from abc import abstractmethod
from pprint import pprint


class Exceptions(ValueError):
    def __init__(self, message):
        self.txt = message


def check_str(value, info):
    if isinstance(value,str):
        return value
    else:
        raise Exceptions(f'Excpected str type for parameter: "{info}" instead of {value} \n')


def check_int(value, info):
    if isinstance(value,int):
        return value
    else:
        raise Exceptions(f'Excpected int type for parameter: "{info}" instead of {value} \n')


def check_amount(number,type,device):
    if number > 0:
        return number
    else:
        raise ValueError(f'{type}{device} out of stock\n')


class Equipment:
    def __init__(self, producer, model, year):
        self.type_obj = self.__class__.__name__
        self.producer = check_str(producer,'Producer')
        self.model = check_str(model, 'Model')
        self.year = check_int(year, 'Year')


    def device_card(self):
        card =  [(self.type_obj),(f'{self.producer} {self.model}'),('Function'),(self.function),('Year'),(self.year)]
        return card


    @abstractmethod
    def function(self):
        pass


class Warehouse:
    def __init__(self, device_card, amount=0):
        self.device_card = device_card
        self.amount = check_int(amount, 'Amount')


    def warehouse(self):
        warehouse = {self.device_card[1]:{'In stock':self.amount,
                                          self.device_card[2] : self.device_card[3], self.device_card[4] : self.device_card[5] }}
        return warehouse


class Printer(Equipment):
    @property
    def function(self):
        function = 'Print'
        return function


class Xerox(Equipment):
    @property
    def function(self):
        function = 'Copy'
        return function


class Scaner(Equipment):
    @property
    def function(self):
        function = 'Scan'
        return function


def warehouse_log(warehouse_dict, device, amount=0):
    device_card = device.device_card()
    log = Warehouse(device_card, amount)
    result = log.warehouse()
    if warehouse_dict.get(device_card[0]):
        warehouse_dict.get(device_card[0]).update(result)
    else:
        warehouse_dict.setdefault(device_card[0],result)
    return warehouse_dict


def departament_log(departamens_dict, warehouse_dict, departament, type, device, amount):
    try:
        device_amount = ((warehouse_dict.get(type)).get(device)).get('In stock')
        result = {device : {'Amount' : amount}}
        if check_amount(device_amount,type,device) >= check_int(amount, 'Amount') :
            (warehouse_dict.get(type).get(device)).update({'In stock':(device_amount-amount)})
            if departamens_dict.get(departament):
                if (departamens_dict.get(departament)).get(type):
                    (departamens_dict.get(departament)).get(type).update({device:{'Amount' : amount}})
                else:
                    (departamens_dict.get(departament)).setdefault(type,result)
            else:
                departamens_dict.setdefault(departament,{type:result})
        else:
            raise ValueError(f'Not enough {type} {device} devices for {departament} departament\n')
    except AttributeError:
        raise ValueError(f'No info about {type} {device} in warehouse\n')
    return departamens_dict


if __name__ == '__main__':
    warehouse_dict = {}
    departamens_dict = {}
    try:
        device_1 = warehouse_log(warehouse_dict, Printer('Canon', 'RV2', 2019), 3)
        device_2 = warehouse_log(warehouse_dict, Printer('HP', 'P1600F', 2021), 2)
        device_3 = warehouse_log(warehouse_dict, Scaner('Apple', 'Jet_1', 2020), 2)
        device_4 = warehouse_log(warehouse_dict, Scaner('Canon', 'F2000', 2019), 4)
        device_5 = warehouse_log(warehouse_dict, Xerox('Digma', 'DV-1', 2019), 3)
        device_6 = warehouse_log(warehouse_dict, Xerox('HP', 'X3000ZT', 2019), 1)
    except Exception as error:
        print(f'ATTENTION: {error}\n')
    print('Warehouse:')
    pprint(warehouse_dict, sort_dicts=False)


    try:
        finance_printers = departament_log(departamens_dict,warehouse_dict,'Finance', 'Printer','HP P1600F', 2)
        finance_scaners = departament_log(departamens_dict, warehouse_dict, 'Finance', 'Scaner', 'Canon F2000', 2)
        trade_printers = departament_log(departamens_dict, warehouse_dict, 'Trade', 'Printer', 'Canon RV2', 3)
        trade_scaners = departament_log(departamens_dict, warehouse_dict, 'Trade', 'Scaner', 'Canon F2000', 2)
        trade_scaners_2 = departament_log(departamens_dict, warehouse_dict, 'Trade', 'Scaner', 'Apple Jet_1', 1)
        trade_xerox =  departament_log(departamens_dict, warehouse_dict, 'Trade', 'Xerox', 'Digma DV-1', 3)
        marketing_scaners = departament_log(departamens_dict, warehouse_dict, 'Marketing', 'Scaner', 'Apple Jet_1', 1)
        marketing_xerox = departament_log(departamens_dict, warehouse_dict, 'Marketing', 'Xerox', 'HP X3000ZT', 1)
    except Exception as error:
        print(f'\nATTENTION: {error}')
    print('\nDepartaments:')
    pprint(departamens_dict, sort_dicts=False)
    print('\nWarehouse:')
    pprint(warehouse_dict, sort_dicts=False)

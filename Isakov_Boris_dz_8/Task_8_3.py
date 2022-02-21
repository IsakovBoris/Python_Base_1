from functools import wraps


def type_logger(func):
    @wraps(func)
    def log_info(*args, **kwargs):
        func_name = func.__name__
        result=str()
        if args:
            for arg in args:
                try:
                    result = f'{result}, {func_name}({arg}: {type(func(arg))})'
                except TypeError:
                    print(f'wrong type of value: {arg} {type(arg)}')
        if kwargs:
            for key in kwargs:
                value=kwargs.get(key)
                try:
                    result = f'{result}, {func_name}({value}: {type(func(value))})'
                except TypeError:
                    print(f'wrong type of value: {value} {type(value)}')
        return result [2:len(result)]
    return log_info


@type_logger
def calc_cube(x):
   return x ** 3


if __name__ == '__main__':
    print(calc_cube(5,2.5,'a',x=10,y='b'))
    print(calc_cube.__name__)

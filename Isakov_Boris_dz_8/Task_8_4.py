from functools import wraps


def val_checker(validation_func):
    def val_checker(calc_cube_func):
        @wraps(calc_cube_func)
        def calc_cube_info(*args):
            for arg in args:
                if validation_func(arg) == True:
                    result = calc_cube_func(arg)
                else:
                    err_msg = f'wrong val: {arg}'
                    raise ValueError(err_msg)
                return result
        return calc_cube_info
    return val_checker


def validation(*args):
    for arg in args:
        if isinstance(arg,int) and arg >= 0:
            check = True
        else:
            check = False
        return check


@val_checker(validation)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube.__name__)
    print(calc_cube('ss'))

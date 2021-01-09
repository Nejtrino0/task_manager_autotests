import allure
import inspect


def manager_params(method, *args, **kwargs):
    required_args = inspect.getfullargspec(method).args
    kw = inspect.getfullargspec(method).varkw
    arg = inspect.getfullargspec(method).varargs
    if kw or arg:
        return args, {**kwargs}

    elif kwargs:
        return [kwargs.get(value) for value in required_args if value != 'self']

    else:
        return args


def wrap_all(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))

        return cls

    return decorate


def step(method):
    def wrapper(self, *args, **kwargs):
        with allure.step(method.__doc__.format(
                manager_params(method, *args, **kwargs)
        )):
            return method(self, *args, **kwargs)

    return wrapper

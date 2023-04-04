import sys
import types
from functools import wraps

from allure_commons.utils import func_parameters
from allure_commons._allure import StepContext


def step(fn: str | types.MethodType | types.FunctionType):
    @wraps(fn)
    def fn_with_logging(*args, **kwargs):
        try:
            is_method = (
                    args
                    and isinstance(args[0], object)
                    and isinstance(getattr(args[0], fn.__name__), types.MethodType)
            )
        except AttributeError as error:
            is_method = False

        args_to_log = args[1:] if is_method else args
        args_and_kwargs_to_log_as_strings = [
            *map(str, args_to_log),
            *[f'{key}={value}' for key, value in kwargs.items()]
        ]

        if 'password' in fn.__name__ or fn.__name__ == 'authorization':
            args_and_kwargs_string = ''
            fn_params = {}
        else:
            args_and_kwargs_string = (
                (': ' + ', '.join(map(str, args_and_kwargs_to_log_as_strings)))
                if args_and_kwargs_to_log_as_strings
                else ''
            )

            fn_params = func_parameters(fn, *args, **kwargs)

        title = (
            (f'[{humanify_class(args[0].__class__.__name__)}] ' if is_method else '')
            + humanify(fn.__name__)
            + args_and_kwargs_string
        )

        step_obj = StepContext(title, fn_params)
        step_obj.__enter__()

        result = fn(*args, **kwargs)

        step_obj.__exit__(*sys.exc_info())

        return result

    return fn_with_logging


def humanify(name: str):
    import re
    return ' '.join(re.split('_+', name)).capitalize()


def humanify_class(name: str):
    new_name = [name[0]]
    for i in range(1, len(name)):
        if name[i].isupper():
            new_name.append(' ' + name[i].lower())
        else:
            new_name.append(name[i])
    return ''.join(new_name)


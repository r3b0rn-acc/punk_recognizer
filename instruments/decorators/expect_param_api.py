import functools
from http import HTTPStatus
from typing import Callable, Any

from django.http import JsonResponse


missing = object()


def expect_param_api(param: str, from_: str = 'collected_params', coerce: Callable = None, default: Any = missing, as_: str = None):
    """
    Декоратор для быстрого описания входных параметров

    :param param: Параметр.
    :param from_: Откуда брать: 'collected_params', 'GET', 'POST'.
    :param coerce: Приведение к нужному типу и валидация.
    :param default: Значение по умолчанию, используется только если параметр при запросе вообще не передан.
    :param as_: Параметр, который будет передан в view, по умолчанию совпадает с 'param'.

    :return: Задекорированная функция с новыми параметрами
    """
    def mediator(view):
        @functools.wraps(view)
        def wrapper(request, *args, **kwargs):
            data = getattr(request, from_)
            if param not in data:
                if default is not missing:
                    value = default
                else:
                    return JsonResponse({'success': False, 'error': f'{param} is required'},
                                        status=HTTPStatus.BAD_REQUEST)
            else:
                value = data[param]
                if coerce is not None:
                    coerce_fn, expected_type = coerce, param
                    try:
                        value = coerce_fn(value)
                    except (ValueError, TypeError) as error:
                        return JsonResponse({'success': False,
                                             'error': f'{repr(value)} is not a valid {expected_type}: {str(error)}'},
                                            status=HTTPStatus.BAD_REQUEST)
            kwargs[as_ or param] = value
            return view(request, *args, **kwargs)
        return wrapper
    return mediator

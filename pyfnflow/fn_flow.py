from .fn_state import FnState
from .fn_result import FnResult, FnOk, FnFail

_FN_TYPE_BIND = "bind"
_FN_TYPE_DO = "do"
_FN_TYPE_AFTER = "after"


# function for bind
def b(bind_key, func):
    return _FN_TYPE_BIND, bind_key, func


# function for do
def d(func):
    return _FN_TYPE_DO, None, func


# function for after
def a(func):
    return _FN_TYPE_AFTER, None, func


def run(functions: list[callable(any)]):
    state = FnState()
    for fn_type, bind_key, func in functions:
        rs = func(state)

        if not isinstance(rs, FnResult):
            print("fn functions always return FnResult object!")
            break

        elif isinstance(rs, FnOk):
            if fn_type == _FN_TYPE_BIND:
                state.set_bind(bind_key, rs.data)
            elif fn_type == _FN_TYPE_DO:
                state.set_result(rs)
            elif fn_type == _FN_TYPE_AFTER:
                pass

        elif isinstance(rs, FnFail):
            if fn_type == _FN_TYPE_BIND:
                pass
                state.set_result(rs)
                break
            elif fn_type == _FN_TYPE_DO:
                pass
                state.set_result(rs)
                break
            elif fn_type == _FN_TYPE_AFTER:
                pass
                state.set_result(rs)
                break
        else:
            pass
    return state.get_result()

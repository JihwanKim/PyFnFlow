from fn_state import FnState
from fn_result import FnResult, FnOk, FnFail

_FN_TYPE_BIND = "bind"
_FN_TYPE_DO = "do"
_FN_TYPE_AFTER = "after"


# fn bind
def b(bind_key, func):
    return _FN_TYPE_BIND, bind_key, func


# fn do
def d(func):
    return _FN_TYPE_DO, func


# fn after
def a(func):
    return _FN_TYPE_AFTER, func


def run(functions: list[callable(any)]):
    state = FnState()
    for fn_type, func in functions:
        rs = func(state)

        if not isinstance(rs, FnResult):
            print("fn functions always return FnResult object!")
            break

        elif isinstance(rs, FnOk):
            if fn_type == _FN_TYPE_BIND:
                state.set_bind(rs.data)
            elif fn_type == _FN_TYPE_DO:
                state.set_result(rs.data)
            elif fn_type == _FN_TYPE_AFTER:
                pass

        elif isinstance(rs, FnFail):
            if fn_type == _FN_TYPE_BIND:
                pass
                state.set_result(rs.data)
                break
            elif fn_type == _FN_TYPE_DO:
                pass
                state.set_result(rs.data)
                break
            elif fn_type == _FN_TYPE_AFTER:
                pass
                state.set_result(rs.data)
                break
        else:
            pass
    state.get_result()

from pyfnflow import fn_flow
from pyfnflow import fn_result


def return_hello():
    return fn_result.FnOk("hello")


def test_fn_flow():
    result = fn_flow.run(
        [
            fn_flow.b("bind_key", lambda _state: return_hello()),
            fn_flow.d(lambda state: fn_result.FnOk(state.get_bind("bind_key"))),
            fn_flow.a(lambda _state: fn_result.FnOk("hello2"))
        ]
    )
    assert result.data == "hello"

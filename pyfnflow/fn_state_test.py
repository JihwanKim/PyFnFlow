from pyfnflow import fn_state, fn_result


# class FnState:
#     def __init__(self):
#         self._state = {}
#
#     # dont call this method
#     def set_bind(self, bind_key: str, bind_value: FnResult) -> any:
#         self._state[bind_key] = bind_value
#
#     # dont call this method
#     def set_result(self, bind_value: FnResult) -> any:
#         self._state['result'] = bind_value
#
#     def get_bind(self, bind_key) -> any:
#         return self._state[bind_key]
#
#     def get_result(self):
#         if 'result' in self._state:
#             return self._state['result']
#         else:
#             return None

class TestFnState:
    def test_fn_state_bind(self):
        state = fn_state.FnState()
        state.set_bind("key1", fn_result.FnOk("hello"))
        state.set_bind("key2", fn_result.FnOk("hello2"))
        assert state.get_bind("key1") == "hello"
        assert state.get_bind("key2") == "hello2"

        state.set_bind("key1", fn_result.FnOk("hello3"))
        assert state.get_bind("key1") == "hello3"

    def test_fn_state_result(self):
        state = fn_state.FnState()
        state.set_result(fn_result.FnOk("hello"))
        result = state.get_result()
        assert isinstance(result, fn_result.FnOk)
        assert result.data == "hello"

        state.set_result(fn_result.FnOk("hello2"))
        result = state.get_result()
        assert isinstance(result, fn_result.FnOk)
        assert result.data == "hello2"

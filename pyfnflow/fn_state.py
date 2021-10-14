from .fn_result import FnResult, FnOk, FnFail


class FnState:
    def __init__(self):
        self._state = {}

    # dont call this method
    def set_bind(self, bind_key: str, bind_value: FnResult) -> any:
        self._state[bind_key] = bind_value

    # dont call this method
    def set_result(self, bind_value: FnResult) -> any:
        self._state['result'] = bind_value

    def get_bind(self, bind_key) -> FnResult:
        bind = self._state[bind_key]
        return bind.data

    def get_result(self):
        if 'result' in self._state:
            return self._state['result']
        else:
            return None

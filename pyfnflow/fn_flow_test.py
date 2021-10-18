from pyfnflow import fn_flow, fn_result


class TestFnFlowBasicFunction:
    def test_bind(self):
        (fn_type, bind_key, _) = fn_flow.b("bind_key", lambda _state: "hello")
        assert fn_type == fn_flow._FN_TYPE_BIND
        assert bind_key == "bind_key"

    def test_do(self):
        (fn_type, _, _) = fn_flow.d(lambda _state: "hello")
        assert fn_type == fn_flow._FN_TYPE_DO

    def test_after(self):
        (fn_type, _, _) = fn_flow.a(lambda _state: "hello")
        assert fn_type == fn_flow._FN_TYPE_AFTER


class TestFnFlowRun:
    @staticmethod
    def ok_with_hello():
        return fn_result.FnOk("hello")

    @staticmethod
    def ok_with_hello2():
        return fn_result.FnOk("hello2")

    @staticmethod
    def fail_with_hello():
        return fn_result.FnFail("hello")

    @staticmethod
    def fail_with_hello2():
        return fn_result.FnFail("hello2")

    def test_run(self):
        result = fn_flow.run(
            [
                fn_flow.b("bind_key", lambda _state: self.ok_with_hello()),
                fn_flow.d(lambda state: fn_result.FnOk(state.get_bind("bind_key"))),
                fn_flow.a(lambda _state: fn_result.FnOk("hello2"))
            ]
        )
        assert isinstance(result, fn_result.FnOk) is True
        assert result.data == self.ok_with_hello().data

        result = fn_flow.run(
            [
                fn_flow.b("bind_key", lambda _state: self.ok_with_hello()),
                fn_flow.b("bind_key", lambda _state: self.ok_with_hello2()),
                fn_flow.d(lambda state: fn_result.FnOk(state.get_bind("bind_key"))),
                fn_flow.a(lambda _state: fn_result.FnOk("hello2"))
            ]
        )
        assert isinstance(result, fn_result.FnOk) is True
        assert result.data == self.ok_with_hello2().data

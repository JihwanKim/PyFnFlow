from pyfnflow import fn_flow


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
    def test_run(self):
        pass

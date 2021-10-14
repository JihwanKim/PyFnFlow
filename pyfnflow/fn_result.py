class FnResult:
    def __init__(self):
        pass


class FnOk(FnResult):
    def __init__(self, data):
        super().__init__()
        self.data = data


class FnFail(FnResult):
    def __init__(self, data):
        super().__init__()
        self.data = data

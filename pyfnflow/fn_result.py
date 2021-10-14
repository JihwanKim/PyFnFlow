class FnResult:
    def __init__(self):
        self.data = None

    def __str__(self):
        return f"FnResult"


class FnOk(FnResult):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def __str__(self):
        return f"FnOk data:{self.data}"


class FnFail(FnResult):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def __str__(self):
        return f"FnFail data:{self.data}"

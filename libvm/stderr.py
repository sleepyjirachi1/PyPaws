###   Standard Error Library   ###


class FatalError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class AssemblerError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

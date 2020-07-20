class BaseError(Exception): ...

class UnknownError(BaseError): ...

class InvalidIDError(BaseError): ...

class NotFoundIDError(BaseError): ...

class NotFoundEnviromentVariableError(BaseError):

    def __init__(self, enviromentVariable):
        self.enviromentVariable : str = enviromentVariable
        self.message = f'The enviroment variable {enviromentVariable} was not found.'
        super().__init__(self.message)

    
    def __str__(self):
        return f'{self.enviromentVariable} -> {self.message}'
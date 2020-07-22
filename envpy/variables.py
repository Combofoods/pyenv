import os, abc, re
import warnings
from typing import TypeVar, Generic
from envpy.error import NotFoundEnviromentVariableError

T = TypeVar('T')

def cleaner(s: str):
    return re.sub('\'|\"' ,'' ,s)


def __text_parser__(text:str) -> dict:
    return {string[0].upper():cleaner(string[1]) for string in [line.split('=', 1) for line in text.splitlines()]}


def __printenv__(variables, preat:bool=True):

    if preat:
        [print(f'{variable} : {variables[variable]}') for variable in variables]


class Variables(object, metaclass=abc.ABCMeta):

    __variables : dict
    prefix: str

    @abc.abstractmethod
    def __load_variables__(self): ...
        # raise NotImplementedError('The sub Class must implement this method')


    def __init__(self, prefix:str=''):
        self.__load_variables__()
        self.prefix = prefix
        self.__filter_variables()


    def printenv(self, preat:bool=True) -> None:
        __printenv__(self.__variables, preat)


    def get_variable(self, variable, conversionType:T=None, defaultValue:str=None) -> T:
        """
        This method exist to help you to check if the desired variable exist if not will return defaultValue.
        Or you can use to get variable.
        TODO.: In the future we will made a type discovery to convert the information from input
        """
        try:
            var = self.__variables[variable]
        except KeyError as _:
            if defaultValue:
                return defaultValue
            else:
                raise NotFoundEnviromentVariableError(variable)
        
        if conversionType:
            return conversionType(var)
        else:
            return var


    def get_all_variables(self, raw: bool = False) -> dict:
        return self.__variables


    def __filter_variables(self) -> None:
        return {variable: self.__variables[variable] for variable in self.__variables if self.prefix in variable}


    def set_variables(self, variables:dict) -> None:
        self.__variables = variables
        
        


class OSVariables(Variables):

    def __load_variables__(self):
        super().set_variables(os.environ)


class FileVariables(Variables):

    file:str
    
    def __load_variables__(self):
        with open(self.file,'r') as data:
            super().set_variables(__text_parser__(data.read()))


    def __init__(self, filepath:str=f'{os.getcwd()}', filename:str='.en', prefix:str=''):
        if not filename :
            raise FileExistsError('The name of file must be valid. Empty values not are allowed.')

        self.file = f'{filepath}/{filename}'
        super().__init__(prefix=prefix)


class Var(Variables):

    variables_file : dict = None
    variables_OS : dict = None

    def __load_variables__(self):
        pass


    def __init__(self, readFile:bool=True, requiredFile:bool=False, readOS:bool=True, filepath:str=f'{os.getcwd()}', filename:str='.env', prefix:str=''):
        

        try:
            if readFile:
                variables_file = FileVariables(filepath=filepath, filename=filename, prefix=prefix).get_all_variables()
        except FileNotFoundError:
            if requiredFile:
                raise FileNotFoundError(f'Missing file: {filepath}/{filename}')
            pass

        try :
            if readOS:
                variables_OS = OSVariables(prefix=prefix).get_all_variables()
        except Exception:
            raise Exception

        if not readFile and readOS:
            super().set_variables(variables_OS)
            return None
        elif readFile and variables_file and not readOS:
            super().set_variables(variables_file)
            return None
        elif not variables_file:
            warnings.warn(f"The {filepath}/{filename} is empty.", UserWarning)

        var = variables_file
        
        for key in set(variables_file).intersection(set(variables_OS)):
            var[key] = variables_OS[key]

        super().set_variables(var)
        

        
        

        

        

        



# if __name__ == "__main__":
#     print(f'Running printenv method')
    # OSVariables().printenv()
    # print(os.path.dirname(os.path.realpath(__file__)))

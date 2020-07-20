import os
from envpy.variables import Var as Variables
from envpy.variables import __printenv__


def get_variables(readFile:bool=True, requiredFile:bool=False, readOS:bool=True, filepath:str=f'{os.getcwd()}', filename:str='.env', prefix:str=''):
    return Variables(readFile=readFile, requiredFile=requiredFile, readOS=readOS, filepath=filepath, filename=filename, prefix=prefix).get_all_variables()


def printenv(variables, preat:bool=True):
    __printenv__(variables, preat)
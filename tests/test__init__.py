import pytest
import envpy
import os

folder = os.path.dirname(__file__)
folder_env_file = f'{folder}/resources'
file_dot_env = 'test.env'


def test__init__():
    karg = {'filepath':folder_env_file, 'filename':file_dot_env}
    envpy.get_variables(**karg)
    envpy.printenv(envpy.get_variables(**karg))




if __name__ == "__main__":
    
    test__init__()
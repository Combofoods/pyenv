# A simple python module to get variables from host or file

## Installing
```
pip install bitbucket-python
```

## Usage
```
from envpy import get_variables

get_variables(readFile:bool=True, requiredFile:bool=False, readOS:bool=True, filepath:str=f'{os.getcwd()}', filename:str='.env', prefix:str='')

```
The method *get_variables* will read the variables from a 'enviroment file' and/or 'enviroment vars' from host system.

The normal behaivior is the method will try to read a 'console current path .env file' if exist and after will check on host if had any enviroment variable with the same name and overide de file value.

Can be change if a enviroment file is or not required. If required will raise a error if the file was not found.

If the readFile or readOS is False the method will ignore the override step.

Also the values can be filter by the use of prefix.



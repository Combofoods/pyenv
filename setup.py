import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='envpy',
      version='0.1',
      description='A simple way to use enviroment configurations.',
      long_description=read('README.md'),
      url='https://github.com/Combofoods/pyenv',
      author='Davi Mello',
      author_email='dsmello.9@gmail.com',
      license='GPL',
      packages=['envpy'],
      zip_safe=False)

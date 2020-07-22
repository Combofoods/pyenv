import os
from setuptools import setup,find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='external-variables',
      version='0.2.1',
      description='A simple way to use enviroment configurations.',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='https://github.com/Combofoods/pyenv',
      author='Davi Mello',
      author_email='dsmello.9@gmail.com',
      license='GPL',
      packages=find_packages(),
      zip_safe=False,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ])

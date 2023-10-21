from setuptools import setup, find_packages

setup(
    name='MyPackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/molive91/myPackage.git',
    author='Olive Manamela',
    author_email='molive91@gmail.com'
)
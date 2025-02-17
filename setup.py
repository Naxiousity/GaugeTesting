"""
Setup Tool for Global Custom Utilities

"""

from setuptools import setup, find_packages

setup(
    name='utils',
    version='2.10.1',
    author='me',
    package_dir={'': 'step_impl'},
    packages=find_packages(where='step_impl', include =['shared', 'shared.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'assertpy==1.1',
        'python-decouple==3.8',
        'pytest==7.4.0',
        'requests==2.31.0',
        'pytest-ordering==0.6',
    ],
    python_requires='3.10.6'
)



from setuptools import setup, find_packages

setup(
    name='BinPy',
    version='0.1.7',
    author='BinPy Developers',
    author_email='binpylib@gmail.com',
    url='http://pypi.python.org/pypi/BinPy/',
    license=open('docs/LICENSE.txt').read(),
    description='Virtualizing Electronics',
    long_description=open('docs/README.txt').read(),
    packages = find_packages(),
    package_data={'data': ['docs/LICENSE.txt','docs/README.txt']},
    include_package_data=True,
    entry_points={'console_scripts':['binpy = BinPy.Shell:shellMain']}
)

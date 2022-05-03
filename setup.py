from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements

setup(
    name='byte',
    packages=find_packages(),
    author='Thanes Ravi',
    include_packages_data=True,
    install_requires=read_requirements(),
    version='0.0.1',
    entry_points='''
    [console_scripts]
    byte=byte.byte:main
    '''
)
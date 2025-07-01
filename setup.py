from setuptools import setup, find_packages

setup(
    name='mini_etl_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'faker',
        'pandas',
        'sqlalchemy',
        'psycopg2-binary'
    ],
    entry_points={
        'console_scripts': [
            'run-etl=main:main',
        ],
    },
)

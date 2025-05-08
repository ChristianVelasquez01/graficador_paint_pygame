from setuptools import setup, find_packages

setup(
    name='graficador_paint_pygame',
    version='5.2.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'graficador_paint_pygame=main.__main__:main',
        ],
    },
)
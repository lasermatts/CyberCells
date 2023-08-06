from setuptools import setup, find_packages

setup(
    name="PyDoku",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'PyDoku=PyDoku:main',
        ],
    },
    install_requires=[
        'numpy',
    ],
    author="Matt Puchalski",
    author_email="me@mattp.tech",
    description="A simple Sudoku game in Python",
    keywords="python sudoku game",
    url="https://github.com/lasermatts/PyDoku",
)

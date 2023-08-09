from setuptools import setup, find_packages

setup(
    name="CyberCells",
    version="0.1.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [

            'CyberCells=CyberCells:main',
            'PyDoku=PyDoku:main',
        ],
    },
    install_requires=[
        'numpy',
    ],
    author="Matt Puchalski",
    author_email="me@mattp.tech",
    description="A simple Cyberpunk inspired Sudoku game",
    keywords="python Cyberpunk sudoku game",
    url="https://github.com/lasermatts/CyberCells",
)

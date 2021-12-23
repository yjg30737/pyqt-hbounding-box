from setuptools import setup, find_packages

setup(
    name='pyqt-horizontal-selection-square-graphics-view',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QGraphicsView with selection box. User can move vertical border of the box horizontally.',
    url='https://github.com/yjg30737/pyqt-horizontal-selection-square-graphics-view.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)
from setuptools import setup, find_packages

setup(
    name='pyqt-textbox-graphics-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt text box which is movable, auto-resizable by text size. Parent class is QGraphicsWidget.',
    url='https://github.com/yjg30737/pyqt-textbox-graphics-widget.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)
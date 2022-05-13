from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-textbox-graphics-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt text box which is movable, auto-resizable by text size. Parent class is QGraphicsWidget.',
    url='https://github.com/yjg30737/pyqt-textbox-graphics-widget.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.8'
    ]
)
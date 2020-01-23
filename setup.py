"""
Color Print
-----------------

ANSII Color formatting to output in terminal.
"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='color_print',
    version='0.1.0',
    url='https://github.com/akhilharihar/python-color-print',
    license='MIT',
    author='Akhil Harihar',
    author_email='hariharakhil@gmail.com',
    description='ANSII Color formatting to output in terminal.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['color_print'],
    python_requires='>=3.0',
    zip_safe=False,
    platforms='any',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Development Status :: 3 - Alpha"
    ]
)

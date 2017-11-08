from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="paramdec",
    version="1.0.0",
    description="Easy parametrized decorators",
    long_description=long_description,
    url="https://github.com/Suenweek/paramdec",
    author="Suenweek",
    author_email="suenweek@protonmail.com",
    license="GPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],
    keywords="development parametrized decorator",
    packages=["paramdec"],
    install_requires=[]
)

from setuptools import setup
from codecs import open
from os import path
import paramdec


here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="paramdec",
    version=paramdec.__version__,
    description="A convenient way to create parametrized decorators.",
    long_description=long_description,
    url="https://github.com/Suenweek/paramdec",
    author=paramdec.__author__,
    author_email=", ".join(author.email for author in paramdec.authors),
    license="GPLv3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],
    keywords="development parametrized decorator",
    packages=["paramdec"],
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)

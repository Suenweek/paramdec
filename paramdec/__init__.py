from collections import namedtuple


Author = namedtuple("Author", ["name", "email"])
Version = namedtuple("Version", ["major", "minor", "patch"])


authors = [
    Author("Roman Novatorov", "suenweek@protonmail.com")
]
version = Version(1, 0, 0)


__version__ = ".".join(map(str, version))
__author__ = ", ".join("%s <%s>" % author for author in authors)


from .paramdec import paramdec


__all__ = ("paramdec",)

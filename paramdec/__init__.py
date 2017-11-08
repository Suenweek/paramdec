from collections import namedtuple


Author = namedtuple("Author", ["name", "email"])


authors = [
    Author("Roman Novatorov", "suenweek@protonmail.com")
]


__version__ = "1.0.0"
__author__ = ", ".join("%s <%s>" % author for author in authors)


from .paramdec import paramdec


__all__ = ("paramdec",)

from setuptools import setup

setup(
    name = "sanesane",
    version="0.0.1",
    author = "Christoph Rissner",
    author_email = "cri@flinkwork.at",
    description = "Sane sane interface to scan stuff.",
    url = "http://www.flinkwork.com",

    install_requires = ["pillow", "pypdf2", "pyinsane"],

    py_modules = ["sanesane"],

    entry_points = {"console_scripts":
                    ["sanesane = sanesane:main",
                    ],
                   }
)

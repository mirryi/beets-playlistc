from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="beets-playlistc",
    version="0.1.1",
    description="A beets plugin to create playlists from query strings",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dophin2009/beets-playlistc",
    author="Eric Zhao",
    author_email="pypa-dev@googlegroups.com",  # Optional
    classifiers=[  # Optional
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Topic :: Multimedia :: Sound/Audio",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="beets plugin",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4",
    install_requires=[
        "beets==1.4.9",
        "jellyfish==0.7.2",
        "munkres==1.1.2",
        "musicbrainzngs==0.7.1",
        "mutagen==1.44.0",
        "pyyaml==5.3.1",
        "six==1.14.0",
        "unidecode==1.1.1",
    ],
    extras_require={
        "dev": [
            "appdirs==1.4.3",
            "attrs==19.3.0",
            "autopep8==1.5.2",
            "black==19.10b0; python_version >= '3.6'",
            "cached-property==1.5.1",
            "cerberus==1.3.2",
            "certifi==2020.4.5.1",
            "chardet==3.0.4",
            "click==7.1.1",
            "colorama==0.4.3",
            "distlib==0.3.0",
            "entrypoints==0.3",
            "flake8==3.7.9",
            "idna==2.9",
            "jedi==0.17.0",
            "mccabe==0.6.1",
            "orderedmultidict==1.0.1",
            "packaging==19.2",
            "parso==0.7.0",
            "pathspec==0.8.0",
            "pep517==0.8.2",
            "pip-shims==0.5.2",
            "pipenv-setup==3.0.1",
            "pipfile==0.0.2",
            "plette[validation]==0.2.3",
            "pycodestyle==2.5.0",
            "pyflakes==2.1.1",
            "pyparsing==2.4.7",
            "python-dateutil==2.8.1",
            "regex==2020.4.4",
            "requests==2.23.0",
            "requirementslib==1.5.7",
            "six==1.14.0",
            "toml==0.10.0",
            "tomlkit==0.6.0",
            "typed-ast==1.4.1",
            "typing==3.7.4.1",
            "urllib3==1.25.9",
            "vistir==0.5.0",
            "wheel==0.34.2",
        ]
    },
    dependency_links=[],
    project_urls={
        "Bug Reports": "https://github.com/Dophin2009/beets-playlistc/issues",
        "Source": "https://github.com/Dophin2009/beets-playlistc",
    },
)

"""
PEP 517 doesn’t support editable installs
so this file is currently here to support "pip install -e ."
"""
from setuptools import setup

setup(
    use_scm_version={"write_to": "blik/_version.py"},
    setup_requires=["setuptools_scm"],
)

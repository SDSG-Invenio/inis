from setuptools import setup

setup(
    name="iaea",
    version="0.1.dev0",
    url="http://iaea.org/inis",
    author="IAEA-SDSG",
    author_email="invenio@invenio-software.org",
    description="INIS Input Management",
    install_requires=[
        "Invenio>=1.9999.4",
    ],
    entry_points={
        "invenio.config": ["iaea = iaea.config"]
    }
)

from setuptools import setup

setup(
    name="inis",
    version="0.1.dev0",
    url="http://inis.iaea.org",
    author="NIS-SDSG",
    author_email="sdsg@iaea.org",
    description="INIS Input Management",
    install_requires=[
        "Invenio>=1.9999.4",
    ],
    entry_points={
        "invenio.config": ["inis = inis.config"]
    }
)

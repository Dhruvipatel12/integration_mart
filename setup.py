from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in indiamart/__init__.py
from indiamart import __version__ as version

setup(
	name="indiamart",
	version=version,
	description="indiamart",
	author="Dhruvi",
	author_email="dhruvi@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

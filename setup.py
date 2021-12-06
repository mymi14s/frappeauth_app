from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappeauth_app/__init__.py
from frappeauth_app import __version__ as version

setup(
	name="frappeauth_app",
	version=version,
	description="Frappe app for authentication, utilities",
	author="Anthony Emmanuel C.",
	author_email="mymi14s@hotmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

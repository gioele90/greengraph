from setuptools import setup, find_packages
with open("README.txt", "rb") as f:
	long_descr = f.read().decode("utf-8")
setup(
	name="greengraph",
	packages=find_packages("greengraph",exclude=["test"]),
	entry_points={
	"console_scripts":['greengraph=greengraph.greengraph:main']
	},
	version="0.1",
	description="Graph the amount of green in a given number of steps between two locations and generate a picture",
	long_description=long_descr,
	author="Gioele Consani",
	install_requires=['argparse','geopy']
	)
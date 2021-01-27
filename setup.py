from setuptools import setup

setup(
    name="pythonpkgtest",
    version="0.0.1-dev",
    description="An example Python Package",
    url="",
    author="7l",
    license="MIT",
    keywords="python setuptools example package installer pip",
    packages=["pythonpkgtest"],
    include_package_data=True,
    install_requires=[
        "python-dotenv",
    ],
)

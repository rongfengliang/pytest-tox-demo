import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="firsttest",
    version="0.0.3",
    author="dalongrong",
    author_email="1141591465@qq.com",
    description="firsttest package",
    long_description=long_description,
    install_requires=['hashids'],
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
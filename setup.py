import setuptools

with open("README.md", "r") as file:
    long_description = file.read()


setuptools.setup(
    name="lessbrew",
    version="0.0.1",
    author="Moein Kareshk",
    author_email="mkareshk@outlook.com",
    description="Brew TL;DR Tutorials",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mkareshk/lessbrew",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    extras_require={"dev": ["pre-commit", "pytest", "pytest-runner", "pytest-cov"]},
    python_requires=">=3.10",
)
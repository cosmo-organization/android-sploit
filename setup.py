import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="android-sploit-sonuaryan", # Replace with your own username
    version="1.0",
    author="Sonu Aryan",
    author_email="sonuaryan76448002@gmail.com",
    description="A package with adb command sets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cosmo-organization/android-sploit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
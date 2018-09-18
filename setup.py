import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="same_size_k_means",
    version="0.0.1",
    author="Nathan Danielsen <nathan.danielsen@gmail.com>",
    author_email="nathan.danielsen@gmail.com",
    license="BSD",
    description="Forked from ndanielsen/same-size-k-means",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Superpedestrian/same-size-k-means",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
    ],
)

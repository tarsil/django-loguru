import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-loguru",
    version="1.0.0",
    author="Tiago Silva",
    author_email="tiago.arasilva@gmail.com",
    description="A middleware to log the requests and responses using loguru.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="git@github.com:tarsil/django-loguru.git",
    packages=setuptools.find_packages(exclude=['tests*']),
    install_requires=["django>=3.1", "loguru"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Framework :: Django :: 3.1"
        "Framework :: Django :: 3.2"
    ],
    python_requires='>=3.7',
)
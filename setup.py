import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="replace-null",
    version="1.0.0",
    author="Lalu Prasad Mahto",
    author_email="lalumahato020@gmail.com",
    description="Pypi module that help you to perform various ml operation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PrasadLalu/ml-operations",
    project_urls={
        "Bug Tracker": "https://github.com/PrasadLalu/ml-operations/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['replace_null', 'stats_models'],
    install_requires=['statsmodels'],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

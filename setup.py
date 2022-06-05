import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-prakashravip1",
    version="1.0.3",
    author="Ravi Prakash",
    author_email="ravip18596@github.com",
    description="Common Python Utility and Client Tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ravip18596/ravi-python-clients",
    project_urls={
        "Bug Tracker": "https://github.com/ravip18596/ravi-python-clients/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

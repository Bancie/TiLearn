from setuptools import find_packages, setup

with open("tilearn/README.md", "r") as f:
    long_description = f.read()

setup(
    name="TiLearn",
    version="0.0.10",
    description="An open-source project for time management and scheduling solutions.",
    package_dir={"": "tilearn"},
    packages=find_packages(where="tilearn"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bancie/TiLearn",
    author="Bancie Ng",
    author_email="chibangn1@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Scheduling",
        "Topic :: Office/Business :: Time Tracking",
        "Topic :: Office/Business :: Machine Scheduling",
        "Topic :: Office/Business :: Time Management",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    # install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["twine>=5.1.1"],
    },
    python_requires=">=3.12.5",
)
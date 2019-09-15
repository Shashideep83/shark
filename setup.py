from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="sharks",
    version="1.0.1",
    description="A Python package for data analysis.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Shashideep83/shark_lib",
    author="Shashi Deep Dulam",
    author_email="shashidulam83@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["sharks"],
    include_package_data=True,
    install_requires=["numpy"],
    
)

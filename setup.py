from setuptools import setup, find_packages

# Read the requirements.txt file to install dependencies
def parse_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Define the setup
setup(
    name="mortage_toolkit_cli",  
    version="0.1.0",           
    description="A simple cli for mortgage cost calculations.",
    long_description=open('README.md').read(),  
    long_description_content_type="text/markdown",  
    author="Joshua Giles",
    author_email="--",
    url="https://github.com/yourusername/yourrepo",  
    packages=find_packages(),  
    install_requires=parse_requirements('requirements.txt'),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
)

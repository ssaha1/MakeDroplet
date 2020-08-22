from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='MakeDroplet',
    version='0.07',
    url='',
    license='',
    author='Saumitra Saha',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'pandas'],
    scripts=['MakeDroplet/RunDroplet.py','MakeDroplet/pdb2xyz.py'],
    python_requires='>=3.5',
    author_email='ssaumitra@gmail.com',
    description='Create a droplet with embeded protein surrounded by water molecule from bulk MD simulation output'
)

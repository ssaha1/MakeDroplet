from setuptools import setup, find_packages

setup(
    name='MakeDroplet',
    version='0.1',
    url='',
    license='',
    author='Saumitra Saha',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'pandas', 'argparse'],
    python_requires='>=3.5',
    author_email='ssaumitra@gmail.com',
    description='Create a droplet with embeded protein sourrounded by water molecule from bulk MD simulation output'
)
from setuptools import setup, find_packages
import subprocess

def requirements():
    with open('requirements.txt') as f:
        return [req.strip() for req in f.readlines()]

setup(
    name="addressline",
    version="0.0.0",
    description="Parsing of an address line into street and housenumber",
    keywords='',
    author="Vagia Rousopoulou",
    author_email="",
    license='',
    packages=find_packages(),
    zip_safe=False,
    install_requires=requirements(),
    scripts=["addressline/test/run_test.py"],
    entry_points={
        'console_scripts': [
            'addressline = addressline.src.cli:main'
        ],
    },
    include_package_data=True
    )

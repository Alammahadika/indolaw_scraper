# setup.py
from setuptools import setup, find_packages

setup(
    name='indolaw_scraper',
    version='0.1.0',
    packages=find_packages(), 
    install_requires=[
        'requests',
        'beautifulsoup4',
        'urllib3',
        
    ],
    author='Alam Mahadika', 
    author_email='alam.mahadika.psm@umy.ac.id', 
    description='A Python package to scrape Indonesian legal documents.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Alammahadika/indolaw_scraper', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)


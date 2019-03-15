import os
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django-italian-utils',
    version='0.3.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Libreria di utility per semplificare la creazione di applicazioni italiane.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/facciocose/django-italian-utils',
    author='Luca Marra',
    author_email='luca@facciocose.it',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

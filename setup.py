import os
from setuptools import setup, find_packages
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-italian-utils',
    version='0.3.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Libreria di utility per semplificare la creazione di applicazioni italiane.',
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

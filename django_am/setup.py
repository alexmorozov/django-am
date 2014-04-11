#--coding: utf8--

from setuptools import setup, find_packages

from django_am import VERSION_STRING

setup(
    name='django-am',
    version=VERSION_STRING,
    description=('Miscellaneous tools for developing and deploying '
                 'Django sites'),
    long_description=open('README.md').read(),
    author='Alex Morozov',
    maintainer='Alex Morozov',
    maintainer_email='inductor2000@mail.ru',
    url='https://github.com/alexmorozov/django-am',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        'Framework :: Django',
        "Topic :: Database :: Front-Ends",
        "Topic :: Documentation",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Operating System :: OS Independent",
    ]
)

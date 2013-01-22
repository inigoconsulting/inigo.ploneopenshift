from setuptools import setup, find_packages
import os

version = '0.2.dev0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='inigo.ploneopenshift',
      version=version,
      description="",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='plone openshift wsgi',
      author='Izhar Firdaus',
      author_email='izhar@inigo-tech.com',
      url='https://github.com/inigoconsulting/inigo.ploneopenshift',
      license='MIT',
      packages=find_packages(),
      namespace_packages=['inigo'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Zope2'
          # -*- Extra requirements: -*-
      ],
      entry_points={
        'paste.app_factory': [
            'main=inigo.ploneopenshift.wsgi:app_factory',
        ]
      }
)

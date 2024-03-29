from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='abstract.geolocationwidget',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Luca Pisani',
      author_email='luca.pisani@abstract.it',
      url='http://www.abstract.it',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['abstract'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

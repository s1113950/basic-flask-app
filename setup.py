#!/usr/bin/env python


from setuptools import setup, find_packages
import versioneer

setup(name='gack',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Github Slack Integration Tool',
      long_description=open('README.md').read(),
      author='Steven Robertson',
      url='https://github.com/s1113950/gack',
      packages=find_packages(),
      install_requires=[
          'pip>=10.0.1',
          'flask>=1.0.2'
      ],
      entry_points={
          'console_scripts': ['gack=gack.main:main']
      })

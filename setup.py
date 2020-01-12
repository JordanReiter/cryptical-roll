from setuptools import setup

setup(name='cryptical_roll',
      version='0.1',
      description='The only die-rolling library that uses cryptographically strong random numbers for rolling dice.',
      url='http://github.com/jordanreiter/cryptical-roll',
      author='Jordan',
      author_email='jordanreiter@gmail.com',
      license='MIT',
      packages=['crypt_roll'],
      scripts=['scripts/crypt-roll'])
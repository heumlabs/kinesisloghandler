from os import path
from setuptools import setup, find_packages
import kinesis_log_handler

REQUIRED_PYTHON = (3, 5)
README = path.abspath(path.join(path.dirname(__file__), 'README.md'))
EXCLUDE_FROM_PACKAGES = ['tests']

setup(
    name='kinesis_log_handler',
    version=kinesis_log_handler.__version__,
    description='Python logging handler for sending logs to AWS Kinesis',
    long_description=open(README).read(),
    install_requires=[
      'boto3'
    ],
    author='Dumok',
    author_email='nsh330@gmail.com',
    url='https://github.com/neillab/kinesis_log_handler',
    license='BSD',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Logging',
    ],
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
)
from setuptools import setup

install_requires = [
    'boto3==1.14.60', 'psycopg2-binary==2.8.6', 'SQLAlchemy==1.3.19'
]

setup(install_requires=install_requires, long_description_content_type='text/x-rst')


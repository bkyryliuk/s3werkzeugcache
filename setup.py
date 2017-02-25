from setuptools import setup, find_packages

version = '0.1.0.0'

setup(
    name='s3werkzeugcache',
    description=(
        "S3 implementation of the werkzeug cache"),
    version=version,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'boto3==1.4.4',
        'flask-cache==0.13.1',
        'werkzeug==0.11.15',
    ],
    author='Bogdan Kyryliuk',
    author_email='b.kyryliuk@gmail.com',
    url='https://git.musta.ch/bogdan-kyryliuk/s3cache',
    download_url=(
        'https://github.com/bogdan-kyryliuk/s3cache/tarball/' + version),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
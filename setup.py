from setuptools import setup, find_packages

version = '0.1.2'

setup(
    name='s3werkzeugcache',
    description=(
        "S3 implementation of the werkzeug cache"),
    version=version,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'boto3',
        'werkzeug',
    ],
    author='Bogdan Kyryliuk',
    author_email='b.kyryliuk@gmail.com',
    url='https://github.com/bkyryliuk/s3werkzeugcache',
    download_url=(
        'https://github.com/bogdan-kyryliuk/s3cache/tarball/' + version),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)

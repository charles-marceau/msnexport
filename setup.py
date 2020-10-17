from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='msnexport',
    version='0.1',
    license="MIT",
    classifiers=["Programming Language :: Python :: 3.7"],
    author='Charles Marceau',
    author_email='charlesmarceau3@gmail.com',
    description='Export your old xml MSN history to pdf.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/charles-marceau/msnexport',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'beautifulsoup4',
        'click',
        'lxml',
        'reportlab'
    ],
    entry_points='''
        [console_scripts]
        msnexport=msnexport.cli:export
    '''
)

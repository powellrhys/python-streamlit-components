from setuptools import setup, find_packages

setup(
    name='streamlit-components',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'streamlit==1.44.0',
        'pandas==2.2.3',
        'azure-storage-blob==12.24.0',
        'plotly==5.24.1'
    ],
    author='Rhys Powell',
    description='A package that defines reuseable streamlit components',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/powellrhys/python-streamlit-components',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)

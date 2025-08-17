from setuptools import setup ,find_packages



setup(
    name='ml_introvert',
    version='0.0.1',
    package_dir={"":'src'},
    package_data=find_packages(where='src')
    )






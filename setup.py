from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='2Dsimulator',
    version='0.0.1',
    description='2D physics simulator for fun (only gravity for now)',
    long_description=readme,
    author='Martin Havelka',
    author_email='mhavelka77@gmail.com',
    license=license,
    packages=find_packages(exclude=('docs'))
)

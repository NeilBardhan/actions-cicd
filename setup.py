from setuptools import setup, find_namespace_packages

install_requirements = [
    'numpy'
]

test_requirements = [
    'pytest',
    'pytest-cov'
]

setup(
    name='demo-py-pkg',
    version='0.0.1',
    description='Demo python package for demonstrating GitHub Actions CI/CD',
    author='neil.bardhan',
    install_requires=install_requirements,
    extras_require={
        "test": test_requirements
    },
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    keywords="demo-py-pkg",
    test_suite="tests",
)
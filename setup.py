from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("torchLBFGS/version.py") as f:
    exec(f.read())

extra_setuptools_args = dict(
    tests_require=['pytest']
)

setup(
    name ='torchLBFGS',
    version = __version__,
    author ='Hao-Jun Michael Shi (Northwestern University) and Dheevatsa Mudigere (Facebook)',
    url = 'git@github.com:stanbiryukov/PyTorch-LBFGS.git',
    install_requires = requirements,
    package_data = {'torchLBFGS':['resources/*']},
    packages = find_packages(exclude=['torchLBFGS/tests']),
    license = 'MIT',
    description='PyTorch-LBFGS: A PyTorch Implementation of L-BFGS',
    long_description= "PyTorch-LBFGS is a modular implementation of L-BFGS, a popular quasi-Newton method, for PyTorch that is compatible with many recent algorithmic advancements for improving and stabilizing stochastic quasi-Newton methods and addresses many of the deficiencies with the existing PyTorch L-BFGS implementation. It is designed to provide maximal flexibility to researchers and practitioners in the design and implementation of stochastic quasi-Newton methods for training neural networks.",
    keywords = ['statistics','matlab','pytorch', 'python', 'lbfgs', 'wolfe'],
    classifiers = [
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License"
    ],
    **extra_setuptools_args
)

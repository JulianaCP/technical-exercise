from setuptools import setup, find_packages

# Used for installing test dependencies directly
tests_require = [
    'flake8',
    'pytest',
]


setup(
    name="data-capture",
    author="Juliana Campos",
    author_email="juliana.campos.parajeles@gmail.com",
    version="0.0.1",
    description="Data capture and stats class.",
    packages=find_packages(exclude=['test']),
    install_requires=[],
    tests_require=tests_require,
    # For installing test dependencies directly
    extras_require={
        'test': tests_require,
    },
    entry_points={
        'console_scripts': []
    },
)

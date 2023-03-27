from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> list[str]:
    """
    This function will return the list of Requirements
    """
    with open(file_path) as file_obj:
        requirements = [req.replace("\n", "") for req in file_obj.readlines()]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="ML_project",
    version="0.0.1",
    author="Amit",
    author_email="Amit.Kumar@unthinkable.co",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

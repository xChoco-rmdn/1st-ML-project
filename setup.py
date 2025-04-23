from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements.
    Reads the requirements from a file and processes each line.
    """
    requirements = []

    # Open the requirements file and read lines
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

        # Strip newline characters from each line
        requirements = [req.strip() for req in requirements]

        # Remove the editable install if it exists
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements  # Return the processed requirements list


setup(
    name='mlproject',
    version='0.0.1',
    author='Rmdn',
    author_email='zulkiflirmdn@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Load requirements dynamically
)

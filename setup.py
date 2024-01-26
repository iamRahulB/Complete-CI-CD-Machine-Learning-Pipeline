from setuptools import setup, find_packages
from typing import List

HYPHON_DOT_E="-e ."

def get_packages(filepath:str )-> List[str]:
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()

        requirements=[var.split("\n")[0] for var in requirements]
        if HYPHON_DOT_E in requirements:
            requirements.remove(HYPHON_DOT_E) 
    return requirements


setup(
    name="ML pipeline",
    version=0.0,
    description="pipeline of model",
    author="rahul bhole",
    author_email="rahulbhole1230@gmail.com",
    packages=find_packages(),
    install_requires=get_packages("requirements.txt"),

)
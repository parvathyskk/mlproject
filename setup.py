from setuptools import find_packages, setup
#from typing import List 

HYPEN_DOT_E ='-e .'

def get_requirements(file_path: str) -> List[str]: 
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        [req.replace("\n", "") for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)
    return requirements

setup(
name='mlproject',
version= '0.0.1',
author= 'parvathyskk',
author_email= 'parvathy3121@gmail.com',
packages= find_packages(), #when find_packages running it checks which folder __init__.py is present 
install_requires=get_requirements('requirements.txt')
)
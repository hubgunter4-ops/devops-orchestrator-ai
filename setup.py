
from setuptools import setup, find_packages

setup(
    name='devops_orchestrator_ai',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'transformers',
        'pydantic',
        'python-dotenv',
        'torch',
    ],
    entry_points={
        'console_scripts': [
            'devops-orchestrator = devops_orchestrator_ai.orchestrator:main',
        ],
    },
    author='Manus AI',
    description='An uncensored AI orchestrator for DevOps tasks and code generation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tu_usuario/devops_orchestrator_ai', # Reemplazar con el repo real
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)

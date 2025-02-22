from setuptools import setup, find_packages

setup(
    name='snuff_assam', 
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'requests',
        # 'random',
        # 'uuid',
        # 'secrets',
        # 'json',
        # 'time',
        # 'urllib'
    ],
    author='Snuff Assam',
    author_email='snuffassam@gmail.com',
    description='Not Available',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',
    url='https://t.me/MrSnuff',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

'setup.py'

from setuptools import setup

setup(
    name='boilerplate1',
    version='0.0.1',
    packages=[],
    py_modules=['listener', 'talker'],
    install_requires=['setuptools'],
    author='Eric Yang',
    author_email='eeyang92@gmail.com',
    maintainer='Eric Yang',
    maintainer_email='eeyang92@gmail.com',
    keywords=['ROS', 'Boilerplate'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='ROS2 Boilerplate V1',
    license='Apache License, Version 2.0',
    test_suite='test',
    entry_points={
        'console_scripts': [
            'listener = listener:main',
            'talker = talker:main',
        ],
    },
)

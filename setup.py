from setuptools import setup

setup(
   name='dockercli',
   version='1.0',
   description='install something to docker container',
   author='greenbear.woo',
   author_email='greenbear.woo@gmail.com',
   packages=['dockercli'],  # would be the same as name
   install_requires=['docker', 'setuptools', 'click'],
   entry_points={
      'console_scripts': ['dockercli = dockercli.main:main']
   },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
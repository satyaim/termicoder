from setuptools import setup,find_packages

def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except:
        pass

setup(
    name='termicoder',
    version='0.1.5.3',
    url='https://github.com/diveshuttam/termicoder',
    author='Divesh Uttamchandani',
    author_email='diveshuttamchandani@gmail.com',
    license='MIT',
    description='a CLI to view, code and submit problems directly from terminal',
    long_description=readme(),
    keywords='competetive iarcs codechef oj',
    classifiers=[
        'Development Status :: 3 - Alpha',
        
        'Intended Audience :: Education',
        'Topic :: Education',
        
        'License :: OSI Approved :: MIT License',
        
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
      ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
        'beautifulsoup4'
    ],
    entry_points='''
        [console_scripts]
        termicoder=termicoder.cli:main
    '''
)

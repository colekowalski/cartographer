from setuptools import setup, find_packages

install_requires = [
    'Django>=2.1,<2.2'
]

setup(
    name='cartographer',
    version='0.0.0.dev0',
    author_email='cole@northernbloc.org',
    url='https://github.com/colekowalski/cartographer',
    description='',
    long_description='',
    license='GPL3',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'cartographer = cartographer.manage:main',
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Security',

        # don't accidently upload to pypi yet
        'nope',
    ],
)

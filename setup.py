from pathlib import Path
from setuptools import setup


def readme():
    this_directory = Path(__file__).parent.resolve()
    with open(this_directory / 'README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name='pytr_api',
    version='0.0.1',
    description='Use TradeRepublic terminal client libraries as API',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/crs/pytr',
    author='Christian Spaniol',
    author_email='christian.spaniol@cpro-iot.com',
    license='MIT',
    packages=['pytr'],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'pytr = pytr.main:main',
        ],
    },
    #  scripts=['traderep'],
    # install_requires=['py_tr'],
    install_requires=[
        'certifi',
        'coloredlogs',
        'ecdsa',
        'packaging',
        'pathvalidate',
        'pygments',
        'requests_futures',
        'shtab',
        'websockets>=10.1',
        'pandas'
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3 :: Only',
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
    zip_safe=False,
)

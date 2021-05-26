from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fgo-bot',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'opencv-python',
        'numpy',
        'matplotlib'
    ],

    author='willC',
    author_email='will7101c@gmail.com',
    description='An automated game bot for Fate Grand Order (CN).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='fgo fate-grand-order auto bot',
    url='https://github.com/will7101/fgo-bot',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
    ]
)

#just a test
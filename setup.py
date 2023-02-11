from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='GoogleNewsAPI',
    packages=find_packages(),
    version='0.0.1',
    license='MIT',
    description='',
    author='uzair-mughal',
    author_email='uzam.dev@gmail.com',
    url='https://github.com/uzair-mughal/google-news-api',
    download_url='https://github.com/uzair-mughal/google-news-api',
    keywords=[
        'Google',
        'News',
    ],
    install_requires=requirements,
    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10'
    ]
)
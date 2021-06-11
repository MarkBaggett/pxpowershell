import setuptools

setuptools.setup(
    name="pxpowershell", 
    version="1.0.0",
    author="MarkBaggett",
    author_email="lo127001@gmail.com",
    description="Interact with Powershell from Python",
    long_description="Interact with a powershell process from Python capturing output of each command.",
    long_description_content_type="text/markdown",
    url="https://github.com/markbaggett/pxpowershell",
    license = "GNU General Public License v3 (GPLv3",
    packages=setuptools.find_packages(),
    package_data={'examples': ['examples']},
    include_package_data=True,
    install_requires = [
        'pexpect>=4.8.0',
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['dir2iso=pxpowershell.example_dir2iso:main'],
    },
    python_requires='>=3.6',
    )
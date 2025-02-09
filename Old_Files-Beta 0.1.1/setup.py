from setuptools import setup, find_packages

setup(
    name="lukaturtle",  # Unique name for your package
    version="0.1.0",          # Package version
    author="Luka Lajnvaš",
    author_email="luka.lajnvas@gmail.com",
    description="A small improvment to turtle, adding the shape function",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LukaLukaLukaLuka/lukaturtle",
    packages=find_packages(),  # Automatically find and include sub-packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Varaždin Center Of Excellence (VCE)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[        # Add dependencies here
    ],
)

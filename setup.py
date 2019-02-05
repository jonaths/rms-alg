import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rms-alg-jonaths",
    version="0.0.1",
    author="Jonathan S. ",
    author_email="author@example.com",
    description="RMS algorithm. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonaths/q_policy_plotter/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
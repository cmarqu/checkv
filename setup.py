import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="checkv",
    use_scm_version={"relative_to": __file__, "write_to": "checkv/version.py"},
    author="Colin Marquardt",
    author_email="cmarqu42@gmail.com",
    description="",
    long_description=long_description,
    url="https://github.com/cmarqu/checkv",
    packages=["checkv"],
    setup_requires=["setuptools_scm"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
    ],
)

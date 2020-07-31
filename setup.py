from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cusbase64",
    version="0.2",
    author="zoemurmure",
    author_email="zoemurmure@gmail.com",
    description="Customized base64 algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zoemurmure/CusBase64",
    py_modules=['cusbase64'],
    entry_points={'console_scripts': [
         'cusbase64 = cusbase64:Cusbase64',
    ]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    zip_safe=False
)
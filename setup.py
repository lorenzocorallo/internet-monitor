import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="internet-monitor",
    version="1.0.2",
    author="Lorenzo Corallo",
    author_email="info@lorenzocorallo.it",
    description="Monitor Internet connectivity and record time and duration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lorenzocorallo/internet-monitor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["internet", "monitor", "uptime", "checker", "online"],
    python_requires='>=3.6',
)
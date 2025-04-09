from setuptools import setup, find_packages

setup(
    name="http-requests",  # Package name
    version="2.25.1",  # Initial version
    packages=find_packages(),  # Find all sub-packages (like http_requests)
    install_requires=[
        "requests>=2.0.0",  # Dependencies for your package
    ],
    author="Your Name",
    author_email="your_email@example.com",
    description="A custom wrapper around the requests library",
    long_description="This package is a custom implementation of http-requests using requests.",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/http-requests",  # Your GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)


from pathlib import Path

from setuptools import find_packages
from setuptools import setup


def main() -> None:
    packages = find_packages(exclude=["tests", "config"])

    setup(
        name="project name",
        description="project description",
        long_description=Path("README.md").read_text(),
        long_description_content_type="text/markdown",
        packages=packages,
        package_data={
            "config": ["gunicorn.conf", "logging.ini"],
        },
        download_url="https://github.com/fxfabre/base_api",
        python_requires=">=3.11",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.11",
        ],
    )


if __name__ == "__main__":
    main()

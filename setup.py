import setuptools
from twcli import __version__

setuptools.setup(
    name="turbowarp-cli",
    version=__version__,
    packages=setuptools.find_packages(),

    entry_points={
        "console_scripts": [
            "twcli=twcli.__main__:main"
        ]
    },
    include_package_data=True,
    author="faretek1",
    description="Run scratch projects in your terminal using turbowarp scaffolding",
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    install_requires=open("requirements.txt").read(),
    keywords=["goboscript", "scratch", "turbowarp"],
    project_urls={
        "Source": "https://github.com/inflated-goboscript/tw-cli",
        "Documentation": "https://inflated-goboscript.github.io/tw-cli/",
        "Homepage": "https://inflated-goboscript.github.io/"
    }
)
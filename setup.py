import setuptools

setuptools.setup(
    name="tw-cli",
    version="v0.0.0",
    packages=setuptools.find_packages(),

    entry_points={
        "console_scripts": [
            "twcli=twcli.__main__:main"
        ]
    },

    author="faretek1",
    description="Run scratch projects in your terminal using turbowarp scaffolding",
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    install_requires=open("requirements.txt").read(),
    keywords=["goboscript", "scratch", "turbowarp"],
    project_urls={
        "Source": "https://github.com/FAReTek1/tw-cli",
        "Documentation": "https://github.com/FAReTek1/tw-cli",
        "Homepage": "https://github.com/FAReTek1/tw-cli/"
    }
)
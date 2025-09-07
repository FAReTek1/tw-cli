import argparse

class Args(argparse.Namespace):
    ...

def main():
    parser = argparse.ArgumentParser(
        prog="twcli",
        description="Run scratch projects in your terminal using turbowarp scaffolding",
        epilog=""
    )

    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", description="run a scratch project")

    args = parser.parse_args(namespace=Args())

    print(args.__dict__)
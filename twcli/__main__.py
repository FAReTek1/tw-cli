import argparse
from typing import Optional
from pathlib import Path

from twcli.run import run, get_exit_code
from twcli import __version__


class Args(argparse.Namespace):
    command: Optional[str]
    project: Optional[str]
    input: Optional[list[str]]
    headed: Optional[bool]
    raise_status: Optional[bool]
    username: str
    project_id: Optional[str]
    cloud_url: str

def main():
    parser = argparse.ArgumentParser(
        prog="twcli",
        description="Run scratch projects in your terminal using turbowarp scaffolding",
        epilog=f"{__version__=}"
    )

    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", description="run a scratch project")
    run_parser.add_argument("project", help="Project path")
    run_parser.add_argument("-i", "--input", nargs="*", dest="input", help="Project input for ask blocks")
    run_parser.add_argument("-H", "--headed", action="store_true", dest="headed", help="Whether to disable headless mode")
    run_parser.add_argument("-U", "--username", nargs="?", dest="username", help="Username for cloud/username block.", default="player")
    run_parser.add_argument("-P", "--project-id", nargs="?", dest="project_id", help="Project id for cloud vars")
    run_parser.add_argument("-C", "--cloud", nargs="?", dest="cloud_url", help="URL for cloud server.", default="wss://clouddata.turbowarp.org")

    args = parser.parse_args(namespace=Args())

    match args.command:
        case "run":
            path = Path(args.project).resolve()
            assert path.exists(), f"Could not find project at {path}"

            print(f"Running {path}")

            print(f"Cloud server = {args.cloud_url}")
            if args.project_id is None:
                args.project_id = path.name
                print(f"Project ID = {args.project_id}")
            print(f"Username = {args.username}")

            if args.input is None:
                args.input = []

            print(f"Args: {args.input}")

            ret = run(path.read_bytes(),
                      args.input,
                      headless=not args.headed,
                      username=args.username,
                      project_id=args.project_id,
                      cloud_host=args.cloud_url)
            code = get_exit_code(ret, "0")

            if code == '1':
                raise RuntimeError(f"Exit code 1; Project failed. Check your logs, and your sb3.")

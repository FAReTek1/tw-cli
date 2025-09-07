import base64
import json
import warnings
from io import TextIOWrapper
from pathlib import Path
from typing import TypedDict, Literal, Optional


class LogMessage(TypedDict):
    type: Literal['log', 'warn', 'error', 'breakpoint', 'exit_code', 'say', 'think']
    content: Optional[str]


__file_path__ = Path(__file__).resolve()
run_html_path = (__file_path__ / '..' / "run.html").resolve()

# noinspection PyProtectedMember
from playwright.sync_api import sync_playwright


def output_msg(msg: LogMessage):
    cat = msg['type']
    content = msg.get('content')

    match cat:
        case 'log':
            print(f"Log: {content!r}")
        case 'warn':
            print(f"Warn: {content!r}")
        case 'error':
            print(f"Error: {content!r}")
        case 'breakpoint':
            print(f"Breakpoint")
        case 'exit_code':
            print(f"Exited with code {content!r}")
        case 'say':
            print(f"Say: {content!r}")
        case 'think':
            print(f"Think: {content!r}")
        case _:
            warnings.warn(f"Unknown message: {msg!r}")
            print(f"{msg['type']}: {msg.get('content', '')!r}")


def run(sb3_file: bytes, input_args_str: str = '', headless: bool = False):
    input_args: list[str] = input_args_str.split('\n')

    def get_arg():
        return input_args.pop(0) if input_args else ''

    with sync_playwright() as playwright:
        chromium = playwright.chromium
        browser = chromium.launch(headless=headless)
        page = browser.new_page()
        page.goto(f"file://{run_html_path}"
                  f"?project={base64.urlsafe_b64encode(sb3_file).decode()}")

        running = True

        def dialogmanage(dialog):
            # when a dialog pops up, we just exit. assume its the end of the program
            nonlocal running
            dialog.accept()
            running = False

        page.on("dialog", dialogmanage)

        output_i = 0  # index of next message

        def get_output() -> list[LogMessage]:
            """
            Handle and return output. If new messages are received, print them.
            """
            nonlocal output_i

            output = page.evaluate("output")
            while len(output) > output_i:
                output_msg(output[output_i])
                output_i += 1

            return output

        while running:
            get_output()

            sc_input = page.query_selector(".sc-question-input")
            if sc_input is not None:
                sc_input.type(get_arg() + '\n')

        return get_output()


if __name__ == '__main__':
    print(run(open("Project.sb3", "rb").read(), """\
faretek
yes
no""", headless=True))  # 0.5
    print(run(open("Project.sb3", "rb").read(), """\
faretek
yes
yes""", headless=True))  # 1.5
    print(run(open("Project.sb3", "rb").read(), """\
faretek
no""", headless=True))  # 1

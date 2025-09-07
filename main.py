import base64
import json
from io import TextIOWrapper
from pathlib import Path

__file_path__ = Path(__file__).resolve()
run_html_path = (__file_path__ / '..' / "run.html").resolve()

# noinspection PyProtectedMember
from playwright.sync_api import sync_playwright

def run(sb3_file: bytes, input_args_str: str = ''):
    input_args: list[str] = input_args_str.split('\n')

    def get_arg():
        return input_args.pop(0) if input_args else ''

    with sync_playwright() as playwright:
        chromium = playwright.chromium
        browser = chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"file://{run_html_path}"
                  f"?project={base64.urlsafe_b64encode(sb3_file).decode()}")

        running = True
        def dialogmanage(dialog):
            nonlocal running
            dialog.accept()
            running = False

        page.on("dialog", dialogmanage)

        def get_output():
            return page.evaluate("output")

        while running:
            sc_input = page.query_selector(".sc-question-input")
            if sc_input is not None:
                sc_input.type(get_arg() + '\n')

        return get_output()

if __name__ == '__main__':
    print(run(open("Project.sb3", "rb").read(), """\
faretek
yes
no"""))  # 0.5
    print(run(open("Project.sb3", "rb").read(), """\
faretek
yes
yes"""))  # 1.5
    print(run(open("Project.sb3", "rb").read(), """\
faretek
no"""))  # 1

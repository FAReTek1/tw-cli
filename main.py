from twcli import run

run(open("Project.sb3", "rb").read(), """\
faretek
yes""") # input last arg manually

run(open("Project.sb3", "rb").read(), """\
faretek
yes
no""")  # 0.5

run(open("Project.sb3", "rb").read(), """\
faretek
yes
yes""")  # 1.5

run(open("Project.sb3", "rb").read(), """\
faretek
no""")  # 1

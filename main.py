from twcli.run import run

# manual

# run(open("Project.sb3", "rb").read(), headless=False)

# not manual

# run(open("Project.sb3", "rb").read(), [
#     "faretek",
#     "yes"
# ])  # input last arg manually

run(open("Project.sb3", "rb").read(), [
    "faretek",
    "yes",
    "no"
]) # 0

run(open("Project.sb3", "rb").read(), [
    "faretek",
    "yes",
    "yes"
])  # 1

run(open("Project.sb3", "rb").read(), [
    "faretek",
    "no"
])  # 1

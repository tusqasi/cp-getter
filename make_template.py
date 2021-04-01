def make_template(URL: str, template_path: str = "../../../templates/py.py"):
    with open(template_path, mode="r") as tmp_file:
        boiler_plate = f"# URL: {URL}\n{tmp_file.read()}"

    with open("sol.py", mode="w") as sol_file:
        sol_file.write(boiler_plate)

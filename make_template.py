def make_template(URL: str):
    with open("../../../templates/py.py", mode="r") as tmp_file:
        boiler_plate = f"# URL: {URL}\n{tmp_file.read()}"

    with open("sol.py", mode="w") as sol_file:
        sol_file.write(boiler_plate)

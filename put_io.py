import os


def put_stuff(tc: dict, i: int):
    """Put test cases"""
    try:
        with open(f"in_{i}.txt", mode="w") as ipf:
            ipf.write(tc["input"])
    except FileExistsError:
        return 1

    try:
        with open(f"out_{i}.txt", mode="w") as opf:
            opf.write(tc["output"])
    except FileExistsError:
        return 1


def put_io(question_name: str, io: list, question_folder: str = "../questions"):
    """Setup putting test cases"""
    os.chdir(question_folder)
    try:
        os.mkdir(question_name)
    except FileExistsError:
        os.chdir(question_name)
        return 1

    # Now in a folder with question_name

    for i, tc in enumerate(io):
        put_stuff(tc, i)

    return 0

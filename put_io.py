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
    finally:
        os.chdir(question_name)

    # Now in a folder with question_name

    for i, tc in enumerate(io):
        put_stuff(tc, i)

    return 0

def test():
    put_io("replacement", [{"input": "10 3\n.b..bz....\n1 h\n3 c\n9 f\n","output": "4\n3\n1\n"},{"input": "4 4\n.cc.\n2 .\n3 .\n2 a\n1 a\n","output": "1\n3\n1\n1\n"}])
if __name__ == "__main__":
    test()
import os


def put_io(question_name: str, io: dict):
    # TODO:

    #   1. Make question folder

    #   2. Make  in.txt, out.txt << put inputs and outputs

    #   3. DONE

    os.chdir("../questions")
    try:
        os.mkdir(question_name)
    except FileExistsError:
        return 0

    os.chdir(question_name)
    # Now in in a folder with question_name

    try:
        with open("in.txt", mode="w") as ipf:
            ipf.write(io["in"])
    except FileExistsError:
        print("File already exists")

    try:
        with open("out.txt", mode="w") as opf:
            opf.write(io["out"])
    except FileExistsError:
        print("File already exists")
    return 1

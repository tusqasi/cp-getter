import os


def put_io(question_name: str, io: dict):
    # TODO:

    #   1. Make question folder

    #   2. Make  in.txt, out.txt << put inputs and outputs

    #   3. DONE

    os.chdir("../questions")
    try:
        os.mkdir(question_name)
    except FileExistsError():
        question_name = question_name.split("_")
        if question_name[-1].isdigit:
            question_name[-1] = str(question_name[-1] + 1)
        else:
            question_name.append("_01")

        question_name = "_".join(question_name)
        os.mkdir(question_name)
    finally:
        os.chdir(question_name)
    # Now in in a folder with question_name

    try:
        with open("in.txt", mode="w") as ipf:
            ipf.write(ipf["in"])
    except FileExistsError():
        print("File already exists")
    finally:
        print("Made test cases inputs")

    try:
        with open("out.txt", mode="w") as opf:
            opf.write(opf["out"])
    except FileExistsError():
        print("File already exists")
    finally:
        print("Made test cases outputs")

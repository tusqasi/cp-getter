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
        if question_name[-1].isdigit():
            question_name = question_name.split("_")
            question_name[-1] = str(int(question_name[-1]) + 1)
            question_name = "_".join(question_name)[0]
        else:
            question_name += "01"

        os.mkdir(question_name)
        print(question_name)

    os.chdir(question_name)
    # Now in in a folder with question_name

    try:
        with open("in.txt", mode="w") as ipf:
            ipf.write(io["in"])
    except FileExistsError:
        print("File already exists")
    finally:
        print("Made test cases inputs")

    try:
        with open("out.txt", mode="w") as opf:
            opf.write(io["out"])
    except FileExistsError:
        print("File already exists")
    finally:
        print("Made test cases outputs")

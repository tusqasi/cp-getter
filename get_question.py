import requests
from bs4 import BeautifulSoup


def get_question(URL):

    return_obj = {"URL":URL}
    return_obj["io"] = dict()
    return_obj["io"]["out"]:str
    return_obj["io"]["in"]:str

    page = requests.get(URL).content

    soup = BeautifulSoup(page, "html.parser")
    parsed_items = []

    for _ in soup.find_all("br"):
        _.replace_with("\n")

    for _ in soup.find_all("pre"):
        parsed_items.append("".join(_.contents))

    for _ in enumerate(parsed_items, start=1):
        if _[0] % 2 == 0:
            return_obj["io"]["out"] = _[1]
        else:
            return_obj["io"]["in"] = _[1]

    return_obj["name"] =  soup.find("div", class_="title").contents[0].split(".", 1)[1][1:].lower()
    

    return return_obj


if __name__ == "__main__":
    print(get_question("https://codeforces.com/contest/1283/problem/B"))

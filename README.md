# **WIP**
___
# cp-getter

cp-getter is a python cli program which setups test cases for a problem on competive programming sites.  
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Installation (only for testing)

git clone this repo to your filesystem  

```bash
git clone https://github.com/tusqasi/cp-getter
```

## Directory structure for now
```bash
├── /Other langs/
├── py
│   ├── cp_problem_getter
│   │   └ main.py
│   └── questions
│       └── /problem_name/
│          ├ in.txt
│          ├ out.tx
│          └ sol.py
│
└── templates
    ├ / other langs templates /
    └ py.py
```
This program makes a new question directory in parent of root directory. Then gets the test cases and then puts them in their questions directory. And also makes a template file to beign your question.
## Usage

```bash
python main.py <URL-OF-PROBLEM>
```

## Contributing
Testing will be appreciated. Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

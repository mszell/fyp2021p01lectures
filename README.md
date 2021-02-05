# First Year Project 2021 @ ITU
## Project 1, Road collisions analysis

In this Github repository you find the code, data, and references used and developed in the lecture for project 1 (Michael Szell). The instructor will push updates as the lecture progresses.

Feel free to clone this repo to have your own copy of everything.

Course page: https://learnit.itu.dk/course/view.php?id=3019694


## Usage

### Development

Startup python3's vitrul environemt which is included in this repo.

#### First and Foremost - Create the virtual environment and install the requirements

*From console in the root of the folder:*

`python -m venv venv`

or

`python3 -m venv venv`

Proceed to activate the environment below and then install the requirements at the end.


#### For Windows Terminal/Powershell

Make the terminal point at the root of the project, then type:

`venv\Scripts\activate.bat`


#### For Linux Terminal

Make the terminal point at the root of the project, then type:


`source venv/bin/activate`

After you've activated the virtual environemt, the command `pip` is globally available.

e.g. `pip search numpy`

To deactivate the virtual environemt, type:

`deactivate`


#### AUTOMACIALLY for Anaconda or Visual Code Studio

In VSCode when opening the notebook, you can select the environemt in the top right corner of the notebook. Here you choose the one that matches the path of the project and is named `venv`.


#### Installing requirements

First update the pip package in the venv:

`python -m pip install -U pip`

`pip install -r requirements.txt`

DONE! You can proceed to use the virtual environment in the console or in your notebook editor.


## Contributors

Constantin-Bogdan Cräciun \<cocr@itu.dk\>

Daniel Hansen \<darh@itu.dk\>

Joao Silva \<joap@itu.dk\>

Thorvald Sørensen \<thso@itu.dk\>

Frederik Raisa \<frai@itu.dk\>
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=flat&logo=gnu-bash&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)

# Automating Initial Project Flow

I just don't wana to do common regular steps to start new project in
local and create repo on github for the same, It just makes me feel bored
to do same steps each time.

I wrote a script using `Python` and `Bash` that is going to create new project on my project folder,
next it will create repo on github for newly created project along with
updating intial README.md file and finaly open visual studio code editior
in my mac.

It's interesting na, I felt the same this script saves lot of time for me.

## Working Demo
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=qZVns0Co-ig)

## Installation

### Install this project in you local

Step #1 Clone this project in your local
`git clone "link"`

step #2 put both files `create.py` and `my_custom_command.sh`
in your home directory

step #3 make `my_custom_command.sh` file excutables run
`chmod +x my_custom_commands.sh` in terminal //for UNIX systems

step #4 make the command available in terminal

    1. Open ~/.bashrc or ~/.zshrc using any text editor you have
    2. Add the following command after the last line or anywhere you want
       source ~/.my_custom_commands.sh

step #5 Make sure to have selenium Install for your python environment
`pip install selenium`

step #6 Open terminal and run `create <project name>` and see the
magic.

Note #1: Make sure to change the path in both files `create.py` and
`my_custom_command.sh` according to your system

Note #2: Make `git` and `visual studio` both added to your system
path, I will recommende check `Automating My Projects with Python.pdf` file present in directory
perform the task under that and make sure everythin is working fine manually.

## Future Scope

In future might be we can add more functionalities to perform taks like commiting and pushing with single line and many more.......

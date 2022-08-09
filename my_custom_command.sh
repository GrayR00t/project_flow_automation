#!/bin/bash
# prints the input
function create() {
    cd  
    python /Users/neerajsingh/Documents/projects/project_automation/create.py $1
    cd /Users/neerajsingh/Documents/projects/$1
    git init
    git remote add origin git@github.com:GrayR00t/$1.git
    touch README.md
    git add .
    git commit -m "Initial Commit"
    git push -u origin master
    code .



  
}


git remote add origin git@github.com:$USERNAME/$1.git
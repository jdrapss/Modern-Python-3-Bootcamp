#!/bin/bash
# Adding, Committing, and Pushing updates to Master for Modern Python 3 Github Repo

echo "What file has been updated?"

read varname

git add $varname

echo "What changes have been made?"
read varname1
git commit -m '($varname1)'
git push origin master

echo "Master has been fed. The beast has been suppressed for another commit."

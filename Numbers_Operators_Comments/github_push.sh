#!/bin/bash
# Adding, Committing, and Pushing updates to Master for Modern Python 3 Github Repo

echo "What file has been updated?"

read varname

git add $varname
git commit -m "New Update to this section"
git push origin master

echo "Master has been fed. The beast has been suppressed for another commit."
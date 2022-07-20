## Tool to rebuild the course outline README

This directory contains a tool (`build_outline.py`) alone with files containing the sequence of days (`days.csv`), the short descriptions of each repo (`descriptions.csv`), additional resources for each repo (`resources.md`), links commonly used in resources (`books.csv`) and a template to insert it all in (`template.md`).

The instructors teaching each individual lesson are in `instructors.csv`. If you are following the main schedule exactly, this is the only one you should modify in your branch. While you can change `README.md` directly after it's been created, it's recommended that changes are made to these files instead.

To use, run do something like:
```
python build_outline.py 1747 Seattle solutions-SEA18 > ../README.md
```
from this directory. The first number is the cohort id in learn, used to generate links to assessments (and possibly other learn material in the future). The campus name is used as the branch for the lecture materials. And the solutions repo is for a link to the solutions repo for the class based on the [directions for creating a solutions branch](https://github.com/GalvanizeDataScience/solutions/blob/master/README.md).

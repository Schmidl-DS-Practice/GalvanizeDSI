import re
import sys
"""
TODO:
    more docstrings
    make less fragile
"""

repo_root = 'https://github.com/GalvanizeDataScience/'
lect_root = 'https://github.com/GalvanizeDataScience/lectures/tree/%campus%/'


def csv_split(line):
    return [field.strip() for field in line.split(',')]


def read_descriptions(filename):
    descriptions = {}
    with open(filename) as f:
        for line in f:
            if line[0] == '#' or not line.strip():
                continue
            repo, description = csv_split(line)
            descriptions[repo] = description
    return descriptions


def read_instructors(filename):
    instructors = {}
    with open(filename) as f:
        for line in f:
            if line[0] == '#' or not line.strip():
                continue
            fields = csv_split(line)
            instructors[fields[0]] = set(fields[1:])
    return instructors


def read_books(filename):
    books = {}
    with open(filename) as f:
        for line in f:
            if line[0] == '#' or not line.strip():
                continue
            book, link = csv_split(line)
            books[book] = link
    return books


def read_resources(filename, books):
    resources = {}
    with open(filename) as f:
        for line in f:
            # comment, skip blank lines
            if line[0] == '#' or not line.strip():
                continue
            # end of file character
            if line[0] == '$':
                break
            if line[0] == '?':
                optional = True
                line = line[1:]
            else:
                optional = False

            fields = csv_split(line)
            if len(fields) >= 3:
                resource, title, link = fields[:3]
                if link in books:
                    link = books[link]
                text = f'[{title}]({link})'
                if len(fields) >= 4:
                    text += f' ({",".join(fields[3:])})'
            else:
                raise ValueError(f'Resources line has {len(fields)} fields: {line}')
            if optional:
                text += '(Optional)'

            if resource not in resources:
                resources[resource] = []
            resources[resource].append(text)
    return resources


def read_days(filename):
    weeks = {}
    with open(filename) as f:
        for line in f.readlines():
            if line[0] == '!':
                week = line[1:].strip()
                weeks[week] = {}
            elif line[0] == '#' or not line.strip():
                continue
            else:
                fields = csv_split(line)
                weeks[week][fields[0]] = fields[1:]
    return weeks


def format_weeks(weeks):
    """Return string with table of contents for the course outline"""
    out = '| Week | Date | Topic |\n| --- | --- | --- |\n'
    for i, week in enumerate(weeks, start=1):
        # generate link text. This is not comprehensive, and should be replaced
        # by whatever is used to generate the html
        link = re.sub('[ :]+', '-', week.strip().lower())
        name = re.sub('.*:', '', week).strip()
        first_day = list(weeks[week])[0]
        # remove day of week. Again, this is fragile
        first_day = re.sub('[ A-Za-z]', '', first_day)
        out += f'| {i} | {first_day} | [{name}](#{link})\n'
    return out


def format_days(weeks, descriptions, instructors, resources):
    """Return string with daily schedule for the course outline"""

    extras = set(resources) - set(descriptions)
    if extras:
        print(f"Warning: Missing Description for repos: {extras}", file=sys.stderr)

    out = ''
    for week in weeks:
        out += f"<br/>\n\n### {week}\n"
        out += "| Day | Readings | Repos | Lecture Materials |\n"
        out += "|:--:|:-----------------------------------------|:--:|:--:|\n"
        for day in weeks[week]:
            out += f'|{day}| '
            repos = weeks[week][day]
            for repo in repos:
                if repo in resources:
                    for resource in resources[repo]:
                        out += resource + ' <br/> '
            out += ' | '
            for repo in repos:
                if not repo:
                    continue
                # is it an actual repo, or just some text?
                if repo[0] == '%':
                    out += repo[1:] + ' <br/> '
                else:
                    out += f'[{descriptions[repo]}]({repo_root + repo}) <br/> '
            out += ' | '
            # NB this is ugly
            time = 'AM'
            repos_no_lecture = set(['weekly-student-led-review',
                                    'feature-branch-git-workflow',
                                    'pandas-eda-case-study',
                                    'spark-case-study',
                                    'regression-case-study',
                                    'supervised-learning-case-study',
                                    'nlp-case-study',
                                    'recommender-case-study',
                                    'fraud-detection-case-study',
                                    'mock-interview-questions'])
            for repo in repos:
                if repo in repos_no_lecture:
                    continue
                if not repo:
                    continue
                if repo[0] == '%':
                    continue
                out += f'[{time}]({lect_root + repo}) <br/> '
                if time == 'AM':
                    time = 'PM'
            out += '|\n'
    return out


def render_template(filename, **kwargs):
    with open(filename) as f:
        text = f.read()
        for kwarg in kwargs:
            text = re.sub(f'\%{kwarg}\%', kwargs[kwarg], text)
    return text


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("""Usage:
python build_outline.py <cohortid>  <campus> <solutions>
Example:
python build_outline.py 1774 Seattle solutions-g120""", file=sys.stderr)
        exit()

    cohortid = sys.argv[1]
    campus = sys.argv[2]
    solutions = sys.argv[3]
    weeks = read_days('days.csv')
    descriptions = read_descriptions('descriptions.csv')
    instructors = read_instructors('instructors.csv')
    books = read_books('books.csv')
    resources = read_resources('resources.csv', books)
    text = render_template('template.md',
                           weeks=format_weeks(weeks),
                           days=format_days(weeks,
                                            descriptions,
                                            instructors,
                                            resources),
                           cohortid=cohortid,
                           campus=campus,
                           solutions=solutions)
    print(text)

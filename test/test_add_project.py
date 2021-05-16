from operator import attrgetter

from model.project import Project
import random
import string


def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    project = Project(name=random_string('Project', 10), description=random_string('Desc', 20))
    app.project.create(project)
    old_projects.append(project)
    new_projects = app.project.get_project_list()
    app.project.open_projects()
    assert sorted(new_projects, key=attrgetter('name')) == sorted(old_projects, key=attrgetter('name'))


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

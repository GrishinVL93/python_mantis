from operator import attrgetter

from model.project import Project
from random import randrange

def test_del_some_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="Project", description="New description"))
    old_projects = app.project.get_project_list()
    index = randrange(len(old_projects))
    app.project.delete_group_by_index(index)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == app.project.count()
    old_projects[index:index+1] = []
    assert sorted(new_projects, key=attrgetter('name')) == sorted(old_projects, key=attrgetter('name'))
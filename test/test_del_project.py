from operator import attrgetter

from model.project import Project
import random

def test_del_some_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="Project", description="New description"))
    old_projects = app.soap.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project)
    new_projects = app.soap.get_project_list()
    old_projects.remove(project)
    assert sorted(new_projects, key=attrgetter('name')) == sorted(old_projects, key=attrgetter('name'))
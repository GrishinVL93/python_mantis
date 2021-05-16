from model import project
from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_projects(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_xpath('//a[text()=\'Manage\']').click()
            wd.find_element_by_xpath('//a[text()=\'Manage Projects\']').click()

    def fill_form_project(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@name='name']").clear()
        wd.find_element_by_xpath("//*[@name='name']").send_keys(project.name)
        wd.find_element_by_xpath("//*[@name='description']").clear()
        wd.find_element_by_xpath("//*[@name='description']").send_keys(project.description)

    def create(self, project):
        wd = self.app.wd
        self.open_projects()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_form_project(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_projects()

    def count(self):
        wd = self.app.wd
        self.open_projects()
        return len(self.get_project_list())

    def get_project_list(self):
        wd = self.app.wd
        self.open_projects()
        sp = []
        elems = wd.find_elements_by_xpath("//table[3]/tbody/tr[@class]")[1:]
        for row in elems:
            name = row.find_element_by_xpath("td/a").text
            description = row.find_element_by_xpath("td[5]").text
            sp.append(Project(name=name, description=description))
        return sp

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_projects()
        self.open_project_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        # confirmation
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def delete_project_by_name(self, project):
        wd = self.app.wd
        self.open_projects()
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_xpath("//div[4]/form/input[3]").click()
        wd.find_element_by_css_selector("input.button").click()


    def open_project_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//a[contains(text(),'Project')]")[index].click()

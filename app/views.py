# -*- coding: utf-8 -*-
import os
from os import listdir
from os.path import isfile
from config import PROJECTS_PATH
from app import app, db
from models import Project
from flask import render_template, redirect, request, Markup
from .forms import NewProjectForm


@app.route('/')
@app.route('/index')
def index():
    projects = Project.query.all()
    return render_template('index.html', title='Cheli Claudio', projects=projects)


@app.route('/project/<name>')
def project(name):
    project = Project.query.filter_by(title=name).first()
    description_file = open(project.description, "r")
    description = Markup(description_file.read());
    description_file.close()
    images_path = PROJECTS_PATH + "/" + project.title + "/images"
    images = [f for f in listdir(images_path) if isfile(os.path.join(images_path, f))]
    images_src = []
    for image in images:
        images_src.append("../static/projects/"+project.title+"/images"+"/"+image)
    return render_template('project.html', project=project, description=description, images=images_src)


@app.route('/projectManager', methods=['GET', 'POST'])
def project_manager():
    new_project_form = NewProjectForm()
    projects = Project.query.all()
    print("project manager")
    if new_project_form.validate_on_submit():
        title = new_project_form.title.data
        print("title: %s" % title)
        print("projects path: %s" % PROJECTS_PATH)
        project_path = PROJECTS_PATH + "/" + title
        project_images_path = project_path + "/images"
        print("project path: %s" % project_path)
        print("project images path: %s" % project_images_path)
        if not os.path.isdir(project_path):
            os.mkdir(project_path)
            os.mkdir(project_images_path)
        else:
            if not os.path.isdir(project_images_path):
                os.mkdir(project_images_path)
            print("folder %s exist" % project_path)

        short_description = new_project_form.shortDescription.data
        description = new_project_form.description.data.replace('\n', '<br>')
        description_file_path = project_path + "/" + title
        print("short description: %s" % short_description)
        print("description: %s" % description)
        print("Save project description in: %s" % description_file_path)
        description_file = open(description_file_path, "w")
        description_file.write(description)
        description_file.close()

        main_image = request.form['image']
        print("main image %s" % main_image)
        for image in request.files.getlist("images"):
            filename = image.filename
            print("image: %s" % filename)
            destination = "/".join([project_images_path, filename])
            print("Save file to: %s" % destination)
            image.save(destination)

        new_project = Project(title=title, shortDescription=short_description,
                              description=description_file_path, mainImage=main_image)
        db.session.add(new_project)
        db.session.commit()
        return redirect('/projectManager')
    else:
        print("form.validate_on_submit() FALSE")
        print(new_project_form.errors)
        for error in new_project_form.title.errors:
            print(error)
        for error in new_project_form.description.errors:
            print(error)
        for error in new_project_form.shortDescription.errors:
            print(error)
    return render_template('projectManager.html', title='Project Manager', form=new_project_form, projects=projects)

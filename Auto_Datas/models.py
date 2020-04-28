# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ProjectApi(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    api_rap_id = models.IntegerField(blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_api'


class ProjectFlow(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    project = models.ForeignKey('Projects', models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_flow'


class ProjectSubFlow(models.Model):
    type = models.CharField(max_length=20, blank=True, null=True)
    step = models.IntegerField()
    process = models.CharField(max_length=1000, blank=True, null=True)
    transmit_dict = models.CharField(max_length=20, blank=True, null=True)
    transmit = models.CharField(max_length=20, blank=True, null=True)
    accept = models.CharField(max_length=20, blank=True, null=True)
    flow = models.ForeignKey(ProjectFlow, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_sub_flow'


class Projects(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    database = models.ForeignKey('ProjectsDatabase', models.DO_NOTHING, blank=True, null=True)
    landfall_location = models.CharField(max_length=20, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects'


class ProjectsDatabase(models.Model):
    type = models.CharField(max_length=20)
    host = models.CharField(max_length=200)
    port = models.CharField(max_length=20, blank=True, null=True)
    server = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects_database'

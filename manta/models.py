# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Anoucments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idthesis = models.ForeignKey('Thesis', models.DO_NOTHING, db_column='idThesis', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anoucments'


class Class(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idprogramstudy = models.ForeignKey('ProgramStudy', models.DO_NOTHING, db_column='idProgramStudy', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    short = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class'


class Faculties(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    short = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faculties'


class Lecturer(models.Model):
    nip = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    username = models.CharField(max_length=255)
    password = models.CharField(db_column='PASSWORD', max_length=255)  # Field name made lowercase.
    gender = models.CharField(max_length=1, blank=True, null=True)
    address = models.CharField(max_length=255)
    private_email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    profile = models.CharField(db_column='PROFILE', max_length=255)  # Field name made lowercase.
    birth_date = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lecturer'


class Meeting(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idthesis = models.ForeignKey('Thesis', models.DO_NOTHING, db_column='idThesis', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=255)
    dates = models.DateField()
    times = models.TimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meeting'


class ProgramStudy(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idfaculty = models.ForeignKey(Faculties, models.DO_NOTHING, db_column='idFaculty', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    short = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'program_study'


class Schedule(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idthesis = models.ForeignKey('Thesis', models.DO_NOTHING, db_column='idThesis', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=255)
    description = models.TextField()
    dates = models.DateField()
    times = models.TimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'


class Students(models.Model):
    nim = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, blank=True, null=True)
    address = models.CharField(max_length=255)
    private_email = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    profile = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class Thesis(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thesis'


class ThesisCordinator(models.Model):
    idthesis = models.OneToOneField(Thesis, models.DO_NOTHING, db_column='idThesis', primary_key=True)  # Field name made lowercase.
    nip = models.ForeignKey(Lecturer, models.DO_NOTHING, db_column='nip')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thesis_cordinator'
        unique_together = (('idthesis', 'nip'),)


class ThesisExaminer(models.Model):
    idthesis = models.OneToOneField(Thesis, models.DO_NOTHING, db_column='idThesis', primary_key=True)  # Field name made lowercase.
    nip = models.ForeignKey(Lecturer, models.DO_NOTHING, db_column='nip')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thesis_examiner'
        unique_together = (('idthesis', 'nip'),)


class ThesisTutor(models.Model):
    idthesis = models.OneToOneField(Thesis, models.DO_NOTHING, db_column='idThesis', primary_key=True)  # Field name made lowercase.
    nip = models.ForeignKey(Lecturer, models.DO_NOTHING, db_column='nip')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thesis_tutor'
        unique_together = (('idthesis', 'nip'),)

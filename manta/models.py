# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Anoucments(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    idthesis = models.ForeignKey('Thesis', models.DO_NOTHING, db_column='idThesis', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anoucments'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Classes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    idstudyprogram = models.ForeignKey('StudyProgram', models.DO_NOTHING, db_column='idStudyProgram', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classes'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Examiners(models.Model):
    idthesis = models.OneToOneField('Thesis', models.DO_NOTHING, db_column='idThesis', primary_key=True)  # Field name made lowercase.
    nip = models.ForeignKey('Lecturer', models.DO_NOTHING, db_column='nip')

    class Meta:
        managed = False
        db_table = 'examiners'
        unique_together = (('idthesis', 'nip'),)


class Faculties(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faculties'


class Lecturer(models.Model):
    nip = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(db_column='PASSWORD', max_length=255)  # Field name made lowercase.
    gender = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    private_email = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    profile = models.CharField(db_column='PROFILE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lecturer'


class MeetManagements(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    link = models.CharField(max_length=255)
    topic = models.CharField(max_length=255, blank=True, null=True)
    result = models.CharField(max_length=255, blank=True, null=True)
    idthesis = models.ForeignKey('Thesis', models.DO_NOTHING, db_column='idThesis', blank=True, null=True)  # Field name made lowercase.
    dates = models.DateField(blank=True, null=True)
    times = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meet_managements'


class Schedules(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    descption = models.TextField(blank=True, null=True)
    idthesis = models.ForeignKey('Thesis', models.DO_NOTHING, db_column='idThesis', blank=True, null=True)  # Field name made lowercase.
    dates = models.DateField(blank=True, null=True)
    times = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedules'


class Students(models.Model):
    nim = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=255)
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    private_email = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    profile = models.CharField(max_length=255, blank=True, null=True)
    idclass = models.ForeignKey(Classes, models.DO_NOTHING, db_column='idClass')  # Field name made lowercase.
    birth_date = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class StudyProgram(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    idfaculty = models.ForeignKey(Faculties, models.DO_NOTHING, db_column='idFaculty', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study_program'


class Thesis(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    nip_cordinator = models.ForeignKey(Lecturer, models.DO_NOTHING, db_column='nip_cordinator')

    class Meta:
        managed = False
        db_table = 'thesis'


class ThesisStudents(models.Model):
    idthesis = models.OneToOneField(Thesis, models.DO_NOTHING, db_column='idThesis', primary_key=True)  # Field name made lowercase.
    nim = models.ForeignKey(Students, models.DO_NOTHING, db_column='nim')

    class Meta:
        managed = False
        db_table = 'thesis_students'
        unique_together = (('idthesis', 'nim'),)


class Tutors(models.Model):
    idthesis = models.OneToOneField(Thesis, models.DO_NOTHING, db_column='idThesis', primary_key=True)  # Field name made lowercase.
    nip = models.ForeignKey(Lecturer, models.DO_NOTHING, db_column='nip')

    class Meta:
        managed = False
        db_table = 'tutors'
        unique_together = (('idthesis', 'nip'),)

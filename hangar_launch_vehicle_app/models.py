from django.db import models

# Create your models here.
class ApplicationComponents(models.Model):
    id_component = models.OneToOneField('Components', models.DO_NOTHING, db_column='id_component', primary_key=True)  # The composite primary key (id_component, id_application) found, that is not supported. The first column is selected.
    id_application = models.ForeignKey('Applications', models.DO_NOTHING, db_column='id_application')

    class Meta:
        managed = False
        db_table = 'application_components'
        unique_together = (('id_component', 'id_application'),)


class Applications(models.Model):
    STATUS_CHOICES = ( 
        (1, 'Черновик'), 
        (2, 'Удален'), 
        (3, 'Сформирован'), 
        (4, 'Завершен'), 
        (5, 'Отклонен'), 
    )

    id = models.AutoField(primary_key=True)
    id_creator = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_creator')
    id_moderator = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_moderator', related_name='applications_id_moderator_set')
    status = models.CharField(max_length=100)
    creation_date = models.DateTimeField()
    formation_date = models.DateTimeField(blank=True, null=True)
    completion_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applications'


class Components(models.Model):
    STATUS_CHOICES = ( 
        (1, 'Удален'), 
        (2, 'Действует'), 
    )
    id = models.AutoField(primary_key=True)
    price = models.TextField()  # This field type is a guess.
    weight = models.BigIntegerField()
    city_production = models.CharField(max_length=100)
    manufacturing_ccompany = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    component_name = models.CharField(max_length=255)
    description = models.TextField()
    image_path = models.TextField()
    category = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'components'


class DjangoMigrations(models.Model):
    id = models.AutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=30)
    adress = models.CharField(max_length=400)
    is_moderator = models.BooleanField()
    login = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'
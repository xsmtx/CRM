# Generated by Django 3.1.4 on 2021-03-27 01:21

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='Parola')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Son Giriş')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='Yönetici Durumu')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Kullanıcı Adı')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='Adı')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Soyadı')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-Posta Adresi')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='Temsilci Durumu')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='Aktif')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Katılma Tarihi')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='Gruplar')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='Kullanıcı İzinleri')),
            ],
            options={
                'verbose_name': 'Kullanıcı',
                'verbose_name_plural': 'Kullanıcılar',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı Adı')),
            ],
            options={
                'verbose_name': 'Temsilci',
                'verbose_name_plural': 'Temsilciler'
            }
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Adı')),
                ('last_name', models.CharField(max_length=20, verbose_name='Soyadı')),
                ('age', models.IntegerField(default=0, verbose_name='Yaşı')),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.agent', verbose_name='Temsilci')),
            ],
            options={
                'verbose_name': 'Müşteri',
                'verbose_name_plural': 'Müşteriler'
            }
        ),
    ]

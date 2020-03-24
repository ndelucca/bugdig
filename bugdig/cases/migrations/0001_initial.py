# Generated by Django 3.0.4 on 2020-03-21 02:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, unique=True)),
                ('description', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('type_of', models.CharField(choices=[('task', 'Task'), ('issue', 'Issue'), ('bug', 'Bug'), ('maintenance', 'Maintenance')], db_index=True, default='task', max_length=12)),
                ('state', models.CharField(choices=[('new', 'New'), ('assigned', 'Assigned'), ('finished', 'Finished')], default='new', max_length=12)),
                ('difficulty', models.SmallIntegerField(choices=[(0, 'Easiest'), (1, 'Easy'), (2, 'Medium'), (3, 'Hard'), (4, 'Hardest')], default=2)),
                ('priority', models.SmallIntegerField(choices=[(0, 'Lowest'), (1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Highest')], default=2)),
                ('assignee', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('cases', django.db.models.manager.Manager()),
            ],
        ),
    ]
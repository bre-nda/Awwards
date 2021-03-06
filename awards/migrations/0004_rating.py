# Generated by Django 3.2.8 on 2021-12-13 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0003_alter_project_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(null=True)),
                ('rate_design', models.PositiveSmallIntegerField(choices=[(10, '10-Outstanding'), (9, '9-Exceeds Expectations'), (8, '8-Excellent'), (7, '7-Good'), (6, '6-Barely Above Average'), (5, '5-Average'), (4, '4-Poor'), (3, '3-Awful'), (2, '2-Dreadful'), (1, '1-Troll')])),
                ('rate_usability', models.PositiveSmallIntegerField(choices=[(10, '10-Outstanding'), (9, '9-Exceeds Expectations'), (8, '8-Excellent'), (7, '7-Good'), (6, '6-Barely Above Average'), (5, '5-Average'), (4, '4-Poor'), (3, '3-Awful'), (2, '2-Dreadful'), (1, '1-Troll')])),
                ('rate_content', models.PositiveSmallIntegerField(choices=[(10, '10-Outstanding'), (9, '9-Exceeds Expectations'), (8, '8-Excellent'), (7, '7-Good'), (6, '6-Barely Above Average'), (5, '5-Average'), (4, '4-Poor'), (3, '3-Awful'), (2, '2-Dreadful'), (1, '1-Troll')])),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

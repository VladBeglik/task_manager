# Generated by Django 3.0.3 on 2020-02-28 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_project_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='rate',
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Project'),
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateField(auto_created=True, null=True),
        ),
    ]

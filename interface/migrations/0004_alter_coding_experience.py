# Generated by Django 5.0.6 on 2024-06-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0003_alter_coding_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coding',
            name='experience',
            field=models.CharField(max_length=20),
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0006_remove_coding_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('birthday', models.DateField(max_length=100)),
                ('nationality', models.CharField(max_length=64)),
                ('languages', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Coding',
        ),
    ]

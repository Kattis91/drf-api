# Generated by Django 3.2.22 on 2023-10-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_uf9lwj', upload_to='images/'),
        ),
    ]

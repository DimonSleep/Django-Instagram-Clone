# Generated by Django 3.2.6 on 2021-08-25 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]

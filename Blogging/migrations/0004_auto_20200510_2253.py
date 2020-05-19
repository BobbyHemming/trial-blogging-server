# Generated by Django 3.0.6 on 2020-05-10 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogging', '0003_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_text',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='user-xxl.jpg', null=True, upload_to=''),
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_user_firstname_remove_user_lastname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('User', 'User')], default='User', max_length=10),
        ),
    ]
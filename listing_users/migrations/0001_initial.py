# Generated by Django 5.1.1 on 2024-10-03 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListingUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('topic', models.CharField(choices=[('home buyer', 'Home Buyer'), ('renter', 'Renter'), ('home seller', 'Home Seller'), ('home owner', 'Home Owner'), ('investor', 'Investor'), ('general industry', 'General Industry')], max_length=30)),
                ('user_description', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]

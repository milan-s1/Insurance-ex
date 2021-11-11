# Generated by Django 3.2.8 on 2021-11-07 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_card_number', models.IntegerField(default=1, unique=True)),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Username', models.CharField(max_length=100)),
                ('Email_address', models.EmailField(default='insuranceex@gmail.com', max_length=254)),
                ('Address', models.CharField(max_length=200)),
                ('Postal_Code', models.IntegerField(default=0)),
                ('Password', models.IntegerField(default=0)),
                ('Phone_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_id', models.IntegerField()),
                ('policy_name', models.CharField(max_length=50)),
                ('policy_period', models.IntegerField()),
                ('policy_price', models.IntegerField()),
                ('policy_description', models.TextField()),
                ('image1', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='user_policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_no', models.IntegerField()),
                ('Aadhar_card_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer')),
                ('policy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.policy')),
            ],
        ),
    ]
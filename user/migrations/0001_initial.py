# Generated by Django 3.2.3 on 2021-05-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=1000)),
                ('bname', models.CharField(max_length=1000)),
                ('bcost', models.IntegerField()),
                ('book_category', models.CharField(choices=[('Programming', 'Programming'), ('Entertainment', 'Entertainment'), ('Others', 'Others')], max_length=50)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('mob', models.CharField(max_length=10)),
                ('add', models.CharField(max_length=10000)),
                ('staff_id', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'orders_table',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_fname', models.CharField(max_length=1000)),
                ('user_email', models.EmailField(max_length=1000)),
                ('user_uname', models.CharField(max_length=1000)),
                ('user_pwd', models.CharField(max_length=1000)),
                ('user_mob', models.CharField(max_length=10)),
                ('user_add', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'users_table',
            },
        ),
    ]
# Generated by Django 3.2.16 on 2022-12-07 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookingListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('due_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]

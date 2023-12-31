# Generated by Django 4.2.7 on 2023-11-04 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food_Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=150)),
                ('category', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('image', models.ImageField(upload_to='Food_Places')),
            ],
        ),
    ]

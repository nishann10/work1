# Generated by Django 5.1.1 on 2024-12-21 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='soft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=100)),
                ('disignation', models.CharField(max_length=100)),
                ('dateofjoin', models.DateField()),
                ('salery', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='image/')),
            ],
        ),
    ]

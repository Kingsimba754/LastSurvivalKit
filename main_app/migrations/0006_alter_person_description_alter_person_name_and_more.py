# Generated by Django 4.1.6 on 2023-02-11 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.TextField(default='What do you know about them?', max_length=250),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default='name?', max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='type',
            field=models.CharField(default='Friend or Foe?', max_length=50),
        ),
    ]

# Generated by Django 4.0.6 on 2022-11-09 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DNF_Showcase', '0002_alter_b_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a',
            name='charfield',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='b',
            name='charfield',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='c',
            name='charfield',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
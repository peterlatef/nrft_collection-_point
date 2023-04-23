# Generated by Django 4.1.7 on 2023-04-07 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defect_register', '0003_defect_cat_alter_defect_defect_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defect',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='defect_cat',
            name='cat',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='defect_weight',
            name='weight',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-31 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0004_auto_20200331_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeplan',
            name='day_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jedzonko.DayName'),
        ),
    ]

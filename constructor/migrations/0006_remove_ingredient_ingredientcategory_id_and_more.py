# Generated by Django 4.2.5 on 2023-09-30 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0005_remove_cocktail_difficulty_remove_cocktail_prep_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='IngredientCategory_id',
        ),
        migrations.DeleteModel(
            name='IngredientCategory',
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-15 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0005_alter_mealperiod_location_alter_menuitem_meal_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealperiod',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meal_periods', to='delta.dininglocation'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='meal_period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='delta.mealperiod'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='menu_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='delta.menuitem'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-14 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField()),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MealPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=18)),
                ('date', models.DateField()),
                ('items_offered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delta.fooditem')),
            ],
        ),
        migrations.AddField(
            model_name='fooditem',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delta.rating'),
        ),
        migrations.CreateModel(
            name='DiningLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=18)),
                ('meal_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delta.mealperiod')),
            ],
        ),
    ]

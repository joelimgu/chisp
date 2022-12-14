# Generated by Django 4.0.5 on 2022-07-03 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_currency_electricalcomponent_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='electricalcomponent',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.currency'),
        ),
        migrations.AlterField(
            model_name='electricalcomponent',
            name='estimated_price',
            field=models.FloatField(default=None, null=True),
        ),
    ]

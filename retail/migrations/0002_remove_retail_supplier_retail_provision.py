# Generated by Django 4.2 on 2023-04-18 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retail',
            name='supplier',
        ),
        migrations.AddField(
            model_name='retail',
            name='provision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='distributors', to='retail.provision', verbose_name='provision'),
        ),
    ]

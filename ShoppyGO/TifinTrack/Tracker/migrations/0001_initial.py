# Generated by Django 4.2 on 2025-04-09 12:37

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('weekday', models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], max_length=10)),
                ('tiffin_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total_tiffins', models.PositiveIntegerField()),
                ('eat_by', multiselectfield.db.fields.MultiSelectField(choices=[('manto', 'Manto'), ('dev', 'Dev'), ('chirag', 'Chirag'), ('pratik', 'Pratik'), ('manan', 'Manan'), ('dhruv', 'Dhruv')], max_length=50)),
                ('per_person_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('manto_wallet', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('dev_wallet', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('chirag_wallet', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('dhruv_wallet', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('manan_wallet', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('pratik_wallet', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

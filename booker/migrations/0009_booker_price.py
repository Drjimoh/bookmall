# Generated by Django 2.2.1 on 2019-06-15 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0008_auto_20190613_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='booker',
            name='price',
            field=models.CharField(choices=[('Free', 'Free'), ('Negotiable', 'Negotiable')], default='Free', max_length=100),
        ),
    ]

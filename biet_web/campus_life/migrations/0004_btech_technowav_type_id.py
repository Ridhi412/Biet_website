# Generated by Django 2.2 on 2020-05-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus_life', '0003_btech_technowav'),
    ]

    operations = [
        migrations.AddField(
            model_name='btech_technowav',
            name='type_id',
            field=models.CharField(default='btect', max_length=10),
            preserve_default=False,
        ),
    ]
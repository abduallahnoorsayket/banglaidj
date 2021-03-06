# Generated by Django 2.1.3 on 2020-04-28 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JWTPayloadTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('iat', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'JWT Payload Tracks',
                'ordering': ['-id'],
            },
        ),
    ]

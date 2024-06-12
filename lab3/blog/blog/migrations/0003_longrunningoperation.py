# Generated by Django 5.0.6 on 2024-06-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LongRunningOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_name', models.CharField(max_length=255)),
                ('data', models.TextField()),
                ('result', models.TextField(blank=True, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]

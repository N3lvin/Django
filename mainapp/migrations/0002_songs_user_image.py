# Generated by Django 5.1.2 on 2024-10-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('artist', models.CharField(max_length=32)),
                ('listeners', models.IntegerField()),
                ('lyrics', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]

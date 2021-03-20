# Generated by Django 3.1.7 on 2021-03-20 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookJournalBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('created_at', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookjournalbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.bookjournalbase')),
                ('num_pages', models.IntegerField()),
                ('janre', models.CharField(max_length=100)),
            ],
            bases=('api.bookjournalbase',),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('bookjournalbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.bookjournalbase')),
                ('type', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
            ],
            bases=('api.bookjournalbase',),
        ),
    ]

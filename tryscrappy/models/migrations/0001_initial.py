# Generated by Django 2.1.7 on 2019-05-30 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('identifier', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('picture', models.ImageField(null=True, upload_to='')),
                ('name', models.CharField(max_length=60)),
                ('birthday', models.DateField(null=True)),
                ('sex', models.BooleanField(null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('scraped', models.BooleanField(default=False)),
                ('brothers', models.ManyToManyField(related_name='person_brothers', to='models.Person')),
                ('father', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_father', to='models.Person')),
                ('friends', models.ManyToManyField(to='models.Person')),
                ('mother', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_mother', to='models.Person')),
                ('sisters', models.ManyToManyField(related_name='person_sisters', to='models.Person')),
            ],
        ),
    ]

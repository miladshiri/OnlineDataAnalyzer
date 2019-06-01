# Generated by Django 2.2 on 2019-05-28 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('machine', '0003_auto_20190528_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('is_public', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('has_label', models.BooleanField(default=True)),
                ('label', models.IntegerField()),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.Data')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.Train')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

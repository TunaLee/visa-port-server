# Generated by Django 3.2.16 on 2023-03-14 20:53

import com_duck.bases.models
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(blank=True, choices=[('', '')], default='', max_length=100, no_check_for_status=True, null=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(blank=True, default=django.utils.timezone.now, monitor='status', null=True, verbose_name='status changed')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='비고')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='활성화 여부')),
            ],
            options={
                'verbose_name': '게시판',
                'verbose_name_plural': '게시판',
                'db_table': 'board',
                'ordering': ['-created'],
            },
            bases=(com_duck.bases.models.UpdateMixin, models.Model),
        ),
    ]

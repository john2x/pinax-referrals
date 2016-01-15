
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils import timezone
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from pinax.referrals.compat import GenericForeignKey


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=100, blank=True, default='')),
                ('code', models.CharField(max_length=40, unique=True)),
                ('expired_at', models.DateTimeField(null=True, blank=True)),
                ('redirect_to', models.CharField(max_length=512)),
                ('target_content_type', models.ForeignKey(to=ContentType, null=True, blank=True)),
                ('target_object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('target', GenericForeignKey(ct_field='target_content_type',
                                             fk_field='target_object_id')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                           related_name="referral_codes",
                                           null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferralResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referral', models.ForeignKey(to='pinax.referrals.Referral',
                                               related_name='responses')),
                ('session_key', models.CharField(max_length=40)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                           null=True)),
                ('ip_address', models.CharField(max_length=45)),
                ('action', models.CharField(max_length=128)),
                ('target_content_type', models.ForeignKey(to=ContentType, null=True, blank=True)),
                ('target_object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('target', GenericForeignKey(ct_field='target_content_type',
                                             fk_field='target_object_id')),
                ('created_at', models.DateTimeField(default=timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

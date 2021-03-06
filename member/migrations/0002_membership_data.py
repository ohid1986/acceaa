# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-11 08:34
from __future__ import unicode_literals


from django.db import models, migrations

MEMBERSHIPS = [
    {
        "category": "General Member",
        "pk": 1,
    },
    {
        "category": "Executive Committee Member",
        "pk": 2,
    },
    {
        "category": "Life Member",
        "pk": 3,
    },]
def add_membership_data(apps, schema_editor):
    Membership = apps.get_model(
        'member', 'Membership')
    for membership_dict in MEMBERSHIPS:
        membership = Membership.objects.create(
            category=membership_dict['category'],
            pk=membership_dict['pk'],)

def remove_membership_data(apps, schema_editor):
    Membership = apps.get_model(
        'member', 'Membership')
    for membership_dict in MEMBERSHIPS:
        membership = Membership.objects.get(
            category=membership_dict['category'],
            pk=membership_dict['pk'],)
        membership.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_membership_data,
            remove_membership_data)
    ]

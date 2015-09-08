from django import forms
from django.db import models
import apps.utils.validators as v


password_field = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "********"}), )
# password_field = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "********"}),
# help_text=v.password.help_text, validators=v.password.validators)


class CSVCharField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['help_text'] = 'Enter mutiple values separated by comma'
        super(CSVCharField, self).__init__(*args, **kwargs)


class CSVTextField(models.TextField):

    def __init__(self, *args, **kwargs):
        kwargs['help_text'] = 'Enter mutiple values separated by comma'
        super(CSVTextField, self).__init__(*args, **kwargs)


def get_fields_and_values(obj):
    data = {}
    fields = obj._meta.fields
    for field in fields:
        value = getattr(obj, field.name)
        data[field.name] = value
    return data


def get_changed_fields(dict1, dict2):
    return [field for field in dict2.keys() if dict1[field] != dict2[field]]

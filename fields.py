# -*- coding: utf-8 -*-
from django.db import models

from django_booley.validators import validate_booley_expression


class BooleyField(models.TextField):

    def validate(self, value, model_instance):
        super(BooleyField, self).validate(value, model_instance)
        return validate_booley_expression(value)
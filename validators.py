# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError

from booley.exceptions import BooleySyntaxError
from booley.parsers import Booley


def validate_booley_expression(expression):
    try:
        parser = Booley()
        return parser.check_syntax(expression)
    except BooleySyntaxError as e:
        raise ValidationError(str(e))
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class CustomPasswordValidator:
    def __init__(self, min_number=2, min_special_char=2, min_length=8):
        self.min_number = min_number
        self.min_special_char = min_special_char
        self.min_length = min_length

    def validate(self, password, user=None):
        special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
        if not len(password)<8:
            raise ValidationError(_('Password must contain at least %(min_length)d character.') % {'min_length': self.min_length})
        if not any(char.isdigit() for char in password):
            raise ValidationError(_('Password must contain at least %(min_number)d digit.') % {'min_number': self.min_number})
        if not any(char in special_characters for char in password):
            raise ValidationError(_('Password must contain at least %(min_special_char)d special character.') % {'min_special_char': self.min_special_char})
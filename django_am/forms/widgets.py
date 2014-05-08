#--coding: utf8--

from django import forms


class SelectDateWidget(forms.TextInput):
    """
    Выбор даты с помощью календаря.
    """
    class Media:
        css = {
            'all': ('am/css/pickmeup.css', ),
        }
        js = (
            'am/js/jquery.pickmeup.min.js',
            'am/js/jquery.pickmeup.settings.js',
        )

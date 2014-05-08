#--coding: utf8--

from django import forms


class SelectDateWidget(forms.DateInput):
    """
    Выбор даты с помощью календаря.
    """
    class Media:
        css = {
            'all': ('django_am/css/pickmeup.css', ),
        }
        js = (
            'django_am/js/jquery.pickmeup.js',
            'django_am/js/jquery.pickmeup.settings.js',
        )

    def __init__(self, attrs=None, format='%d.%m.%Y'):
        final_attrs = {
            'class': 'pickmeupwidget',
            'data-pmu-format': 'd.m.Y',
            'data-input-mask': '99.99.9999',
            'size': '10',
        }
        if attrs is not None:
            final_attrs.update(attrs)
        super(SelectDateWidget, self).__init__(attrs=final_attrs,
                                               format=format)


class CKEditorWidget(forms.Textarea):
    """
    Виджет визуального редактора.
    """
    def __init__(self, attrs=None):
        super(CKEditorWidget, self).__init__(attrs)
        if 'class' in self.attrs:
            self.attrs['class'] += ' ckeditor'
        else:
            self.attrs['class'] = 'ckeditor'

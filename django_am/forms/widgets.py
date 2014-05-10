#--coding: utf8--

from django import forms
from django.template.loader import render_to_string


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


class ImagePreviewWidget(forms.ClearableFileInput):
    """
    Виджет загрузки картинки с ее превью.
    """
    template_name = 'django_am/image_preview_widget.html'
    thumbnail_preset = '50x50'

    def render(self, name, value, attrs=None):
        context = dict(
            input=forms.FileInput.render(self, name, value, attrs),
            field=self,
            name=name,
            value=value,
            attrs=attrs,
            thumbnail_preset=self.thumbnail_preset,
            checkbox_name=self.clear_checkbox_name(name),
        )
        context.update(
            checkbox_id=self.clear_checkbox_id(context['checkbox_name']))
        return render_to_string(self.template_name, context)

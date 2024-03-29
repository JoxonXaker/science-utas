from django.db import models

from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
    

class AboutModel(models.Model):
    title = models.CharField(_('title'), max_length=50, null='', blank='')
    description = models.CharField(_('description'), max_length=150, default='definitely change that!')
    detail = models.TextField(_('detail'), null='', blank='')
    url = models.URLField(_('url'), null=True, blank=True)

    def __str__(self) -> str:
        return self.detail


# class ContactModel(models.Model):
#     title = fields.TranslationField(
#         models=models.CharField(name=_('about title'), max_length=150, null='', blank=''),
#         language='en',
#         empty_value=''
#     )
#     detail = fields.TranslationField(
#         RichTextField(name=_('about detail'), null='', blank=''),
#         language='en',
#         empty_value=''
#     )



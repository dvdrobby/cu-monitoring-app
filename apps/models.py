from django.db import models
from django.utils.text import slugify

class FormModel(models.Model):
    form_name = models.CharField(max_length=100)
    form_slug = models.SlugField(blank= True , editable= False)

    def save(self):
        self.form_slug = slugify(self.form_name)
        super(FormModel, self).save()

    def __str__(self):
        return self.form_name

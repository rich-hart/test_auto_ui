from django.db import models

class PDFs(models.Model):
    pdf = models.FileField(upload_to='pdfs/')

class CVTest(models.Model):
    pdf_a = models.ForeignKey('PDFs')
    pdf_b = models.ForeignKey('PDFs')
    options = models.CharField()
    results = TextField()


# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from django.forms.extras.widgets import SelectDateWidget

SERVICE_CHOICES = (
	('','Servicio de interés'),
	('estudios-mercado','Estudio de Mercado'),
	('sondeo-opinion-publica','Sondeo de opinión pública'),
	('asesoria-mercadotecnia', 'Asesoría en mercadotecnia'),
	('hispanic-market-research', 'Hispanic market research'),
	('apoyo-logistico-campo', 'Apoyo logístico de campo'),
	('productos-focus', 'Productos focus'))

class EmailWidget(forms.widgets.Input):
    input_type = 'email'
    required = 'required'
    
class ContactForm(forms.Form):
	name = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class':'custom_textbox', 'required':'required'}))
	position = forms.CharField(max_length=140, required=False, widget=forms.TextInput(attrs={'class':'custom_textbox'}))
	company = forms.CharField(max_length=140, required=False, widget=forms.TextInput(attrs={'class':'custom_textbox'}))
	location = forms.CharField(max_length=140, required=False, widget=forms.TextInput(attrs={'class':'custom_textbox'}))
	email = forms.EmailField(max_length=140, widget=EmailWidget(attrs={'required':'required', 'class': 'custom_textbox'}))
	telephone = forms.CharField(max_length=40, required=False, widget=forms.TextInput(attrs={'class':'custom_textbox'}))
	service = forms.MultipleChoiceField(required=False, widget=forms.Select, choices=SERVICE_CHOICES)
	message = forms.CharField(max_length=400, widget=forms.Textarea(attrs={'required':'required'}))

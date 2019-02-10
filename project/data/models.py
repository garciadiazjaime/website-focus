# -*- coding: utf-8 -*-

from django.db import models
import json

class Section(models.Model):
	LANG_CHOICES = ((0,'Spanish'), (1,'English'),)

	title = models.CharField(max_length=140)
	slug = models.CharField(max_length=140, unique=True)
	in_menu = models.BooleanField(default=False)
	in_footer = models.BooleanField(default=False)
	weight_menu = models.IntegerField(blank=True, null=True)
	weight_footer = models.IntegerField(blank=True, null=True)
	lang = models.IntegerField(choices=LANG_CHOICES, default=0)

	def __unicode__(self):
		return str(self.title)

class Data(models.Model):
	text = models.TextField(blank=True, null=True)
	section =  models.ForeignKey(Section)

	def __unicode__(self):
		return unicode(self.text)

class SolutionsManager(models.Manager):
	def all_json(self, lang):
		response  = []
		if lang == 0:
			response = {
				'estudios-mercado': {
					'title': 'Estudios de<br /> mercado',
					'items': {'imagen-posicionamiento':[], 'factibilidad-mercado':[], 'habitos-mercado':[], 'evaluacion-servicio-cliente':[], 'analisis-competencia':[], 'evaluacion-campanas-publicitarias':[], 'auditoria-servicio':[], 'censos-comerciales-mapas':[], 'grupos-foco':[]}, 				
				},	
				'sondeos-opinion-publica': {
					'title': 'Sondeos de<br> opinión pública',
					'items' :{'imagen-posicionamiento':[], 'encuestas-electorales-politicas':[], 'imagen-personajes-publicos':[], 'encuestas-opinion':[]}, 
				},
				'asesoria-mercadotecnia': {
					'title': 'Asesoría en<br> mercadotecnia',
					'items': {'pruebas-ideas-conceptos':[], 'panel-mercadologos':[], 'asesoria-mercadotecnia':[]},
				},
				'hispanic-market-research': {
					'title': 'Hispanic market<br> research',
					'items': {'hispanic-market-research':[]},
				},
				'apoyo-logistico-campo': {
					'title': 'Apoyo logístico',
					'items': {'apoyo-logistico-campo':[]}, 
				},
				'productos-focus': {
					'title': 'Productos<br> focus',
					'items': {'unibus':[], 'previa':[], 'camara-gesell':[]},
				},
			}
		else:
			# ENG
			response = {
				'market-studies': {
					'title': 'Market<br /> studies',
					'items': {'image-positioning':[], 'market-feasibility':[], 'consumption-habits':[], 'customer-service':[], 'competition-analysis':[], 'advertising-campaign-assessment':[], 'service-audit':[], 'commercial-censuses-maps':[], 'focus-group':[]}, 				
				},	
				'public-opinion-polls': {
					'title': 'Public <br> opinion polls',
					'items' :{'goverment-image-perception':[], 'electoral-political-surveys':[], 'public-figure-image':[], 'opinion-polls':[]}, 
				},
				'marketing-advisory': {
					'title': 'Marketing <br> Advisory',
					'items': {'idea-concept-tests':[], 'marketers-panel':[], 'marketing-advisory':[]},
				},
				'hispanic-market-research2': {
					'title': 'Hispanic market<br> research',
					'items': {'hispanic-market-research':[]},
				},
				'field-logistical-support': {
					'title': 'Field <br>logistical support',
					'items': {'field-logistical-support':[]}, 
				},
				'focus-products': {
					'title': 'Focus<br> products',
					'items': {'unibus-survey':[], 'previa-software':[], 'gesell-chamber':[]},
				},
			}
		for row in self.filter(lang=lang):
			response[row.solution]['items'][row.url].append({
				'title': row.title,
				'subtitle': row.subtitle,
				'text': row.text,
				'url': row.url,
				'id': row.id,
				})
		return json.dumps(response)

class Solutions(models.Model):
	SOLUTION_CHOICES = (
		('estudios-mercado','es - estudios-mercado'), 
		('sondeos-opinion-publica','es - sondeos-opinion-publica'),
		('asesoria-mercadotecnia', 'es - asesoria-mercadotecnia'),
		('hispanic-market-research', 'es - hispanic-market-research'),
		('apoyo-logistico-campo', 'es - apoyo-logistico-campo'),
		('productos-focus', 'es - productos-focus'),
		
		('market-studies','en - estudios-mercado'), 
		('public-opinion-polls','en - sondeos-opinion-publica'),
		('marketing-advisory', 'en - asesoria-mercadotecnia'),
		('hispanic-market-research2', 'en - hispanic-market-research'),
		('field-logistical-support', 'en - apoyo-logistico-campo'),
		('focus-products', 'en - productos-focus'),
	)
	LANG_CHOICES = ((0,'Spanish'), (1,'English'),)
	title = models.CharField(max_length=140)
	subtitle = models.CharField(max_length=140, blank=True, null=True)
	text = models.TextField(blank=True, null=True)
	url = models.CharField(max_length=140)
	solution = models.CharField(choices=SOLUTION_CHOICES, default=0, max_length=140)
	objects = models.Manager()
	custom = SolutionsManager()
	lang = models.IntegerField(choices=LANG_CHOICES, default=0)

	def __unicode__(self):
		return unicode(self.title)

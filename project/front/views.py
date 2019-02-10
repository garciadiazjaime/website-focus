# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import HttpResponse, render_to_response
from survey.models import Question, Answer, Response
from data.models import Section, Data, Solutions
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template import RequestContext
from models import ContactForm
from misce import send_contact_message
from datetime import date
from twitter import *
import os
import json


def home(request, lang=0):
	'''
		function to show home view
		lang = 0:Esp, 1:Eng
	'''
	page = get_lang_labels('esp','inicio') if lang == 0 else get_lang_labels('eng','home')
	data = Data.objects.filter(section=1).order_by('id') if lang == 0 else Data.objects.filter(section=6).order_by('id')
	gral_data = Data.objects.filter(section=13) if lang == 0 else Data.objects.filter(section=14)
	year = date.today().year
	main_menu = Section.objects.filter(in_menu=True, lang=lang).order_by('weight_menu')
	footer_menu = Section.objects.filter(in_footer=True, lang=lang).order_by('weight_footer')
	question = Question.objects.filter(active=True, lang=lang).order_by('-reg_date')[0]
	answer = question.answer_set.filter(active=True)
	return render_to_response('section/home.html', locals(), context_instance=RequestContext(request))

def about_us(request, lang=0, tag=''):
	'''
		function to show about us view
		lang = 0:Esp, 1:Eng
	'''
	page = get_lang_labels('esp','nosotros') if lang == 0 else get_lang_labels('eng','about-us')
	data = Data.objects.filter(section=2).order_by('id') if lang == 0 else Data.objects.filter(section=7).order_by('id')
	gral_data = Data.objects.filter(section=13) if lang == 0 else Data.objects.filter(section=14)

	year = date.today().year
	main_menu = Section.objects.filter(in_menu=True, lang=lang).order_by('weight_menu')
	footer_menu = Section.objects.filter(in_footer=True, lang=lang).order_by('weight_footer')
	question = Question.objects.filter(active=True).order_by('-reg_date')[0]
	answer = question.answer_set.filter(active=True)
	return render_to_response('section/about_us.html', locals())

def solutions(request, lang=0, solution='estudios-mercado', product=''):
	'''
		function to show solutions view
		lang = 0:Esp, 1:Eng
	'''
	page = get_lang_labels('esp','soluciones') if lang == 0 else get_lang_labels('eng','solutions')

	if product != '':
		extra_solution_sp_url = '/' + solution + '/' + product
		extra_solution_en_url = '/' + translate_solution(lang, solution) + '/' + translate_product(lang, product)


	data = Data.objects.filter(section=3).order_by('id') if lang == 0 else Data.objects.filter(section=8).order_by('id')

	gral_data = Data.objects.filter(section=13) if lang == 0 else Data.objects.filter(section=14)
	solutions = Solutions.custom.all_json(lang)

	year = date.today().year
	main_menu = Section.objects.filter(in_menu=True, lang=lang).order_by('weight_menu')
	footer_menu = Section.objects.filter(in_footer=True, lang=lang).order_by('weight_footer')
	question = Question.objects.filter(active=True).order_by('-reg_date')[0]
	answer = question.answer_set.filter(active=True)

	list_products = Solutions.objects.filter(solution=solution)
	desc_product = Solutions.objects.filter(solution=solution, url=product)[0] if len(product) else ''

	return render_to_response('section/solutions.html', locals())

def translate_solution(lang, solution):
	data = [
		{
			'estudios-mercado': 'market-studies',
			'sondeos-opinion-publica': 'public-opinion-polls',
			'asesoria-mercadotecnia': 'marketing-advisory',
			'apoyo-logistico-campo': 'field-logistical-support',
			'productos-focus': 'focus-products'
		},
		{
			'market-studies': 'estudios-mercado',
			'public-opinion-polls': 'sondeos-opinion-publica',
			'marketing-advisory': 'asesoria-mercadotecnia',
			'field-logistical-support': 'apoyo-logistico-campo',
			'focus-products': 'productos-focus'
		}
	]
	return data[lang][solution]

def translate_product(lang, product):
	data = [
		{
			'imagen-posicionamiento': 'image-positioning',
			'factibilidad-mercado': 'market-feasibility',
			'habitos-mercado': 'consumption-habits',
			'evaluacion-servicio-cliente': 'customer-service',
			'analisis-competencia': 'competition-analysis',
			'auditoria-servicio': 'advertising-campaign-assessment',
			'evaluacion-campanas-publicitarias': 'service-audit',
			'censos-comerciales-mapas': 'commercial-censuses-maps',
			'grupos-foco': 'focus-group',

			'imagen-posicionamiento': 'goverment-image-perception',
			'encuestas-electorales-politicas': 'electoral-political-surveys',
			'imagen-personajes-publicos': 'public-figure-image',
			'encuestas-opinion': 'opinion-polls',

			'pruebas-ideas-conceptos': 'idea-concept-tests',
			'panel-mercadologos': 'marketers-panel',
			'asesoria-mercadotecnia': 'marketing-advisory',

			'apoyo-logistico-campo': 'field-logistical-support',

			'unibus': 'unibus-survey',
			'previa': 'previa-software',
			'camara-gesell': 'gesell-chamber'
		},
		{
			'image-positioning': 'imagen-posicionamiento',
			'market-feasibility': 'factibilidad-mercado',
			'consumption-habits': 'habitos-mercado',
			'customer-service': 'evaluacion-servicio-cliente',
			'competition-analysis': 'analisis-competencia',
			'advertising-campaign-assessment': 'auditoria-servicio',
			'service-audit': 'evaluacion-campanas-publicitarias',
			'commercial-censuses-maps': 'censos-comerciales-mapas',
			'focus-group': 'grupos-foco',

			'goverment-image-perception': 'imagen-posicionamiento',
			'electoral-political-surveys': 'encuestas-electorales-politicas',
			'public-figure-image': 'imagen-personajes-publicos',
			'opinion-polls': 'encuestas-opinion',

			'idea-concept-tests': 'pruebas-ideas-conceptos',
			'marketers-panel': 'panel-mercadologos',
			'marketing-advisory': 'asesoria-mercadotecnia',

			'field-logistical-support': 'apoyo-logistico-campo',

			'unibus-survey': 'unibus',
			'previa-software': 'previa',
			'gesell-chamber': 'camara-gesell'
		}
	]
	return data[lang][product]

def products(request, lang=0, tag=''):
	'''
		function to show solutions view
		lang = 0:Esp, 1:Eng
	'''
	page = get_lang_labels('esp','productos') if lang == 0 else get_lang_labels('eng','products')
	data = Data.objects.filter(section=11).order_by('id') if lang == 0 else Data.objects.filter(section=12).order_by('id')
	gral_data = Data.objects.filter(section=13) if lang == 0 else Data.objects.filter(section=14)
	year = date.today().year
	main_menu = Section.objects.filter(in_menu=True, lang=lang).order_by('weight_menu')
	footer_menu = Section.objects.filter(in_footer=True, lang=lang).order_by('weight_footer')
	question = Question.objects.filter(active=True).order_by('-reg_date')[0]
	answer = question.answer_set.filter(active=True)
	return render_to_response('section/products.html', locals())

def contact(request, lang=0, email_response=''):
	'''
		function to show contact view
		lang = 0:Esp, 1:Eng
	'''
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			send_contact_message(request)
			return HttpResponseRedirect('/contacto/gracias')
	else:
		form = ContactForm()

	page = get_lang_labels('esp','contacto') if lang == 0 else get_lang_labels('eng','contact')
	data = Data.objects.filter(section=4).order_by('id') if lang == 0 else Data.objects.filter(section=9).order_by('id')
	gral_data = Data.objects.filter(section=13) if lang == 0 else Data.objects.filter(section=14)
	year = date.today().year
	main_menu = Section.objects.filter(in_menu=True, lang=lang).order_by('weight_menu')
	footer_menu = Section.objects.filter(in_footer=True, lang=lang).order_by('weight_footer')
	question = Question.objects.filter(active=True).order_by('-reg_date')[0]
	answer = question.answer_set.filter(active=True)
	return render_to_response('section/contact.html', locals(), context_instance=RequestContext(request))

def send_email(request, lang=0):
	response = {
		'status': False
	}
	if request.method == 'POST':
		result = send_contact_message(request)
		if result.status_code == 200:
			response['status'] = True

	return HttpResponse(json.dumps(response), content_type="application/json")

def focus_usa(request, lang=0):
	'''
		function to show focus usa view
		lang = 0:Esp, 1:Eng
	'''
	page = get_lang_labels('esp','focus-usa') if lang == 0 else get_lang_labels('eng','focus2-usa')
	data = Data.objects.filter(section=5).order_by('id') if lang == 0 else Data.objects.filter(section=10).order_by('id')
	gral_data = Data.objects.filter(section=13) if lang == 0 else Data.objects.filter(section=14)
	year = date.today().year
	main_menu = Section.objects.filter(in_menu=True, lang=lang).order_by('weight_menu')
	footer_menu = Section.objects.filter(in_footer=True, lang=lang).order_by('weight_footer')
	question = Question.objects.filter(active=True).order_by('-reg_date')[0]
	answer = question.answer_set.filter(active=True)
	return render_to_response('section/focus_usa.html', locals())

def coverage(request, lang=0):
	'''
		function to show focus usa view
		lang = 0:Esp, 1:Eng
	'''
	page = get_lang_labels('esp','cobertura') if lang == 0 else get_lang_labels('eng','coverage')
	data = Data.objects.filter(section=2).order_by('id') if lang == 0 else Data.objects.filter(section=7).order_by('id')
	gral_data = Data.objects.filter(section=13) if lang == 0 else Data.objects.filter(section=14)
	year = date.today().year
	main_menu = Section.objects.filter(in_menu=True, lang=lang).order_by('weight_menu')
	footer_menu = Section.objects.filter(in_footer=True, lang=lang).order_by('weight_footer')
	question = Question.objects.filter(active=True).order_by('-reg_date')[0]
	answer = question.answer_set.filter(active=True)
	return render_to_response('section/coverage.html', locals())

def privacy(request, lang=0):
	gral_data = Data.objects.filter(section=13) if lang == 0 else Data.objects.filter(section=14)
	year = date.today().year
	main_menu = Section.objects.filter(in_menu=True, lang=lang).order_by('weight_menu')
	footer_menu = Section.objects.filter(in_footer=True, lang=lang).order_by('weight_footer')
	print footer_menu
	return render_to_response('section/privacy.html', locals())

def get_lang_labels(lang, flag):
	'''
		function to set page array (sp,en), it helps to actived the correct menu item and set lang links
	'''
	response = {}
	data = {
		'esp': ['inicio', 'nosotros', 'soluciones', 'productos', 'contacto', 'focus-usa', 'cobertura'],
		'eng': ['home', 'about-us', 'solutions','products', 'contact', 'focus2-usa', 'coverage'],
	}
	index = data[lang].index(flag)
	response = {'local': data['esp'][index], 'foreign': data['eng'][index]} if lang == 'esp' else {'local': data['eng'][index], 'foreign': data['esp'][index]}
	return response

@csrf_exempt
def get_last_tweets(request):
	import re
	OAUTH_TOKEN = os.environ['TW_OAUTH_TOKEN']
	OAUTH_SECRET = os.environ['TW_OAUTH_SECRET']
	CONSUMER_KEY = os.environ['TW_CONSUMER_KEY']
	CONSUMER_SECRET = os.environ['TW_CONSUMER_SECRET']
	response = ''
	i = 1;
	t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
	tmp = t.statuses.user_timeline()
	for row in tmp:
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', row['text'])
		if urls[0] and len(urls[0]):
			row['text'] = row['text'].replace(urls[0], '<a href="' + urls[0] + '" target="_blank">' + urls[0] + '</a>')
		response += "<div><p>" + row['text'] + "</p><p id=\"twitter_follow\"><a href=\"https://twitter.com/focus_bc\" target=\"_blank\">Seguir a @FOCUSinvestigacion</a></p>"
		response += "<br><br></div>"
		if i == 5: break
		i += 1
	return HttpResponse(response)

@csrf_exempt
def survey_answer(request, lang=0):
	'''
		function to save user response and return survey results
	'''
	response = ''
	user_answer = request.POST.get('answer', '')
	if user_answer:
		r = Response(answer_id=user_answer)
		r.save()

		values = []
		total = 0
		user_selected_votes = 0
		survey_answers = Answer.objects.filter(question=r.answer.question)
		for row in survey_answers:
			votes = Response.objects.filter(answer=row).count()
			total += votes
			if str(row.id) == str(user_answer):
				user_selected_votes = votes
			values.append({
				'value': row.value,
				'votes': votes,
				})
		percentage = user_selected_votes * 100 / total
		response = {'status': True, 'percentage': percentage, 'survey': values, 'answer': r.answer.value}
	else:
		response = {'status': False}
	return HttpResponse(json.dumps(response), content_type="application/json")

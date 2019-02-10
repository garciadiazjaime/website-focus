/*
    AUTHOR: MINT IT MEDIA
    http://mintitmedia.cm
*/

var folder = '/';
var server = get_server_path() + folder;

$(document).ready(function () {

  var page = get_currentpage();
  var last_item = getLastItem(page);

  if ($('#survey_question').length) load_survey();

  if ($('#hidden_menu.nosotros').length || $('#hidden_menu.about-us').length) load_scroll_menu();

  if ($('#nosotros_slider').length) load_bullet_slider();

  if ($('.carousel').length) $('.carousel').carousel()

  if ($('#gesell_slider').length) {
    load_bullet_slider('#gesell_slider');
  }

  if ($('#focus_group_slider').length) {
    load_bullet_slider();
  }

  if ($('#view_more_history').length) load_history();

  if ($('#reasons_accordeon').length) load_acordeon();

  if ($('#clients_agencies').length) load_clients();

  // solution & product grid
  if ($('#solutions_main_wrapp').length && page.indexOf('inicio') == -1 && page.indexOf('home') == -1) load_soluciones();

  if ($('#map_tj_title').length) load_map();

  if ($('#slider_conocenos').length) load_full_slider();

  if ($('#solutions_slider').length) load_full_slider("solutions_slider");

  if ($('#conoce-mas-focus').length) load_link_aboutus();

  if ($('#twitter_feed').length) get_last_tweets()


  if ($('#' + last_item).length) {
    var group_a = ['experiencia', 'historia', 'equipo', 'infraestructura', 'experience', 'history', 'team', 'infraestructure']
    if (group_a.indexOf(last_item) != -1) {
      gotoTop(last_item, 120);
    }
    if (last_item == 'apoyo-logistico-campo' || last_item == 'field-logistical-support') {
      gotoTop(last_item, 900);
    } else {
      gotoTop(last_item);
    }
  }

  loadHomePage();

  loadContactForm();
});

function get_last_tweets() {
  $.post('get_last_tweets', function (data) {
    $('#twitter_feed').html(data);
    $('#twitter_feed').cycle({
      fx: 'scrollDown',
      timeout: 10000,
      cleartypeNoBg: true
    });
  });
}

function load_link_aboutus() {
  $("#conoce-mas-focus").click(function () {
    gotoTop("why-focus", 20);

    return false
  });
}

function load_map() {
  // 0: tj; 1: mx; 2: usa
  var maps = [
    '<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3364.38746736385!2d-117.01881!3d32.515797!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80d94838414a57f7%3A0x180d6a74a830db0c!2sAv+la+Santa+Maria!5e0!3m2!1sen!2sus!4v1393785217209" width="100%" height="100%" frameborder="0" style="border:0"></iframe>',
    '<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3359.147192203205!2d-115.408373!3d32.655527!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x3610fb6d112ef8e8!2sCetys+Universidad!5e0!3m2!1sen!2s!4v1404407336236" width="100%" height="100%" frameborder="0" style="border:0"></iframe>',
    '<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3360.159900961091!2d-116.96569199999999!3d32.628565!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80d945993a303303%3A0x98fe9e154a973a2b!2s2127+Olympic+Pkwy+%231006!5e0!3m2!1sen!2sus!4v1393741024434" width="100%" height="100%" frameborder="0" style="border:0"></iframe>'
  ]

  $("#map_ctrl p").click(function () {
    if ($(this).data('map') != $('#map_tj').data('map')) {
      $('#map_ctrl').find('.active').removeClass('active');
      $('#map_tj').html(maps[$(this).data('map')]);
      $(this).addClass('active');
      $('#map_tj').data('map', $(this).data('map'))
    }
  });

  $('#map_tj').html(maps[0]);
}

function load_clients() {
  $("#clientes_list").click(function () {

    $("#clients_agencies li").removeClass("active");
    $("#agencies_list_logos").removeClass("active fadeIn").addClass("fadeOut");
    $("#association_list_logos").removeClass("active fadeIn").addClass("fadeOut");

    $(this).addClass("active");
    $("#clients_list_logos").addClass("active fadeIn").removeClass("fadeOut");

  });

  $("#agencies_list").click(function () {

    $("#clients_agencies li").removeClass("active");
    $("#clients_list_logos").removeClass("active fadeIn").addClass("fadeOut");
    $("#association_list_logos").removeClass("active fadeIn").addClass("fadeOut");

    $(this).addClass("active");
    $("#agencies_list_logos").addClass("active fadeIn").removeClass("fadeOut");


  });

  $("#association_list").click(function () {

    $("#clients_agencies li").removeClass("active");
    $("#clients_list_logos").removeClass("active fadeIn").addClass("fadeOut");
    $("#agencies_list_logos").removeClass("active fadeIn").addClass("fadeOut");

    $(this).addClass("active");
    $("#association_list_logos").addClass("active fadeIn").removeClass("fadeOut");


  });

}

function load_scroll_menu() {
  if ($('#hidden_menu').offset()) {
    var sticky_navigation_offset_top = 680;
  }
  var sticky_navigation = function () {
    var scroll_top = $(window).scrollTop();
    scroll_top += 18;
    if (scroll_top > sticky_navigation_offset_top) {
      $('#hidden_menu').css({
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'opacity': 1
      });
    } else {
      $('#hidden_menu').css({
        'position': 'fixed',
        'top': 5000,
        'opacity': 0
      });
    }

  };
  sticky_navigation();
  $(window).scroll(function () {
    sticky_navigation();
  });
}

function load_history() {
  $("#view_more_history").click(function () {
    $("#extra_history").show('slow');
    $("#view_more_history").addClass("hidden");
    return false;
  });
  $("#view_less_history").click(function () {
    $("#extra_history").hide('slow');
    $("#view_more_history").removeClass("hidden");
    return false;
  });

}

function load_soluciones() {
  $("#btn_soluciones").click(function (e) {
    e.preventDefault();
    $("#listado_soluciones").addClass("active");
    $("#bloque_servicios").removeClass("active");
  });

  $("#listado_soluciones a").click(function (e) {
    if ($(this).parent().parent().attr('id') != "hispanic") {
      e.preventDefault();

      $("#bloque_servicios").addClass("active");
      $("#listado_soluciones").removeClass("active");
      var solution = update_product_info($(this).attr('href'));

      if (!Object.keys) {
        Object.keys = function (obj) {
          var keys = [];
          for (var i in obj) {
            if (obj.hasOwnProperty(i)) {
              keys.push(i);
            }
          }
          return keys;
        };
      }
      var keys = Object.keys(solutions[solution]['items']);

      $('#services_header').html(solutions[solution]['title']).addClass(solution);
      $('#services_list').html('');
      var products = order_products(solution, keys);
      var product = getLastItem($(this).attr('href'));
      var url = $(this).attr('href');
      var page = url.indexOf('solucion') != -1 ? 'soluciones' : 'solutions';

      for (var i = 0; i < keys.length; i++) {
        if (products[i].url == product) {
          $('#services_list').append('<li class="active ' + products[i].url + '""><a href="/' + page + '/' + solution + '/' + products[i].url + '" title="' + products[i].title + '">' + products[i].title + '</a></li>');
        } else {
          $('#services_list').append('<li class="' + products[i].url + '""><a href="/' + page + '/' + solution + '/' + products[i].url + '" title="' + products[i].title + '">' + products[i].title + '</a></li>');
        }
      }

      load_product_click();
      setTimeout(function () {
        if (product == 'grupos-foco' || product == 'focus-group' || product == 'camara-gesell' || product == 'gesell-chamber' || product == 'previa' || product == 'previa-software') {
          load_bullet_slider();
        }
      }, 300)
    }
  });

  $("#next, #next_mobile").click(function (e) {
    e.preventDefault();
    var current_product = $('#menu_servicios').find('.active');
    if ($(current_product).next('li').length) {
      var next_product = $(current_product).next('li').children();
      $(next_product[0]).click();
    } else {
      var first_li = $(current_product).parent().children()
      var first_product = $(first_li[0]).children()
      $(first_product[0]).click();
    }
  });

  // if the bloque_servicios has class active then load its click
  if ($('#bloque_servicios').hasClass('active')) {
    load_product_click();
    gotoTop('bloque_servicios', 90);
  }
}


function load_product_click() {
  $('#services_list a').click(function (e) {
    e.preventDefault();
    update_product_info($(this).attr('href'));

    $('#menu_servicios').find('.active').removeClass('active');
    $(this).parent().addClass('active');
    var local_this = this;

    setTimeout(function () {
      if ($(local_this).attr('href').indexOf('grupos-foco') != -1 || $(local_this).attr('href').indexOf('focus-group') != -1 || $(local_this).attr('href').indexOf('camara-gesell') != -1 || $(local_this).attr('href').indexOf('gesell-chamber') != -1) {
        load_bullet_slider();
      }
    }, 300);

  })
}

function order_products(solution, keys) {
  var response = '';
  var data = [],
    tmp = [];
  var i = 0,
    j = 0;
  for (i = 0; i < keys.length; i++) {
    data[i] = {
      'id': solutions[solution]['items'][keys[i]][0].id,
      'title': solutions[solution]['items'][keys[i]][0].title,
      'url': solutions[solution]['items'][keys[i]][0].url
    };
  }
  for (i = 0; i < data.length - 1; i++) {
    for (j = i + 1; j < data.length; j++) {
      if (data[i].id > data[j].id) {
        tmp = data[i];
        data[i] = data[j];
        data[j] = tmp;
      }
    }
  }
  return data;
}

function update_product_info(href) {
  var product = getLastItem(href);
  var solution = getLastItem(href.replace('/' + product, ''));

  if (typeof (window.history.pushState) != 'undefined') {
    window.history.pushState(href, href, href);
  }
  gotoTop('bloque_servicios', 90);

  $('#service_title').html(solutions[solution]['items'][product][0].title);
  $('#service_subtitle').html(solutions[solution]['items'][product][0].subtitle);
  $('#service_desc').html(solutions[solution]['items'][product][0].text);
  $('#services_content').removeClass().addClass('offset1').addClass('span7').addClass(product);

  update_lang_url(href)
  return solution;
}

/*
	function to update url on lang when user clicks on a product, all this happens in the FE
	this helps on solution page
*/
function update_lang_url(href) {
  if (href.indexOf('solucion') != -1) {
    var items = href.split('/');
    var url = '/' + items[1] + '/' + items[2] + '/' + items[3];
    var translate_url = '/solutions/' + translate_solution(0, items[2]) + '/' + transalte_product(0, items[3]);

    $($('#lang a')[0]).attr('href', url);
    $($('#lang a')[1]).attr('href', translate_url);
  } else if (href.indexOf('solution') != -1) {
    var items = href.split('/');
    var url = '/' + items[1] + '/' + items[2] + '/' + items[3];
    var translate_url = '/soluciones/' + translate_solution(1, items[2]) + '/' + transalte_product(1, items[3]);

    $($('#lang a')[1]).attr('href', url);
    $($('#lang a')[0]).attr('href', translate_url);
  }
}

function translate_solution(lang, solution) {
  data = [{
    'estudios-mercado': 'market-studies',
    'sondeos-opinion-publica': 'public-opinion-polls',
    'asesoria-mercadotecnia': 'marketing-advisory',
    'apoyo-logistico-campo': 'field-logistical-support',
    'productos-focus': 'focus-products'
  }, {
    'market-studies': 'estudios-mercado',
    'public-opinion-polls': 'sondeos-opinion-publica',
    'marketing-advisory': 'asesoria-mercadotecnia',
    'field-logistical-support': 'apoyo-logistico-campo',
    'focus-products': 'productos-focus'
  }]
  return data[lang][solution]
}

function transalte_product(lang, product) {
  var response = '';
  var data = [{
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
  }, {
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
  }];
  return data[lang][product];
}

function load_full_slider(my_id) {

  var id = (my_id) ? my_id : "slider_conocenos";
  var mouseEnteredSlider = false;
  var slider = $('#' + id).cbpFWSlider({
    speed: 200, // default transition speed (ms)
    easing: 'ease' // default transition easing
  }).mouseenter(function () {
    mouseEnteredSlider = true;
  }).mouseleave(function () {
    mouseEnteredSlider = false;
  });

  setInterval(function () {
    if (!mouseEnteredSlider) {
      if ($('.cbp-fwnext').css('display') != 'none') {
        $('.cbp-fwnext').click();
      } else {
        $('.cbp-fwdots span:first-child').click();
      }
    }
  }, 10000);

}


function load_vert_slider(my_id, prev, next) {
  var id = (my_id) ? my_id : "vert_slider"; //siempre será id, asignar sin símbolo
  var prev_name = (prev) ? prev : "prev_btn"; //siempre será id, asignar sin símbolo
  var next_name = (next) ? next : "next_btn"; //siempre será id, asignar sin símbolo


  $("#" + id).cycle({
    fx: 'fade',
    speed: 'fast',
    timeout: 0,
    next: "#" + next_name,
    prev: "#" + prev_name
  });
}

function load_bullet_slider(my_id, my_nav_id) {
  var id = (typeof (my_id) != "undefined") ? my_id : ".bullet_slider"; //puede ser clase o id, incluir símbolo
  var nav_id = (typeof (my_nav_id) != "undefined") ? my_nav_id : "bullet_nav"; //siempre sera id, sin símbolo
  $(id).after('<div id="' + nav_id + '" class="bullets">').cycle({
    fx: 'fade',
    speed: 'slow',
    pager: "#" + nav_id
  });
}

function load_acordeon() {
  $("#reasons_accordeon > li > h3").click(function () {
    $('#reasons_accordeon div').slideUp(300);
    if (false == $(this).next().is(':visible')) {

      $('#reasons_accordeon h3').css({
        'background-position': "right 10px"
      });
      $('#reasons_accordeon div').hide('slow');

      $(this).next().show('slow');
      $(this).css({
        'background-position': "right -40px"
      });

    } else {
      $(this).css({
        'background-position': "right 10px"
      });
    }
  });
  $('#reasons_accordeon div').hide();
  $('#reasons_accordeon h3').css({
    'background-position': "right 10px"
  });

  $('#reasons_accordeon div:eq(0)').show();
  $('#reasons_accordeon h3:eq(0)').css({
    'background-position': "right -40px"
  });
}

/*
	Function to handlel survey behavio, POST AJAX, JS EFFECT
*/
function load_survey() {
  $('#survey_question a').click(function (e) {
    e.preventDefault();
    var option_selected = $(this).attr('rel')
    var response_option = $(this).data('opt')
    var lang = $('#lang').data('lang');
    var content_response = '';
    $.post('/survey_answer', {
      'answer': option_selected
    }, function (data) {
      //survey_green
      content_response = (lang == 0) ?
        'de nuestros usuarios eligieron el ' + data.answer + '<br /> <p class=\"pverde\">Símbolo de nuestro profesionalismo, ética e impacialidad.</p><p class=\"pazul\">Símbolo de nuestro compromiso, objetividad e imparcialidad.</p><a href=\"/nosotros\">Conócenos de cerca</a>' :
        'of our users selected ' + data.answer + '<br /> <p class=\"pverde\">Symbol of our professionalism, ethics and fairness.</p><p class=\"pazul\">Symbol of our professionalism, ethics and fairness.</p><a href=\"/about-us\">About us</a>';

      $('#survey_response').html('<div class=\"' + response_option + '\"><div class=\"wrap\">' + '<div class=\"percentage\">' + data.percentage + '%</div>' + content_response + '</div></div>');
      var green_width_buffer = (data.percentage / 100) * 803 + ($(window).width() - 803) / 2;
      var green_width = response_option == 'response_a' ? green_width_buffer : $(window).width() - green_width_buffer;
      var blue_width = $(window).width() - green_width;
      if (response_option == 'response_a') {
        //selected green
        $('#survey_response .response_a').width(green_width);
      } else {
        //selected blue
        $('#survey_response .response_b').width(blue_width);

      }


      $('#survey_green').animate({
        'width': green_width + 'px'
      });
      $('#survey_question').find('a').addClass('hide');
    });
  })
}

/*
	function to get current page ex- /contact, /about-us
*/
function get_currentpage() {
  var loc = window.location;
  p = loc.href.substring(loc.href.indexOf(loc.host) + loc.host.length + folder.length);
  if (p == '') p = 'inicio';
  return p;
}

/*
	to move scroll to specif element tag,
	you can add an offset value if necessary to affect the final position
*/
function gotoTop(id, offset) {
  var offset_val = (offset) ? offset : 0;
  if (id.length)
    $('html, body').animate({
      scrollTop: $('#' + id).delay(800).offset().top - offset_val
    }, 'slow');
}

/*
	function to get last parameter from URL
*/
function getLastItem(cadena) {
  var params = cadena.split('/');
  return params.pop();
}

/*
	function to get url server
*/
function get_server_path() {
  var loc = window.location;
  return "http://" + loc.hostname;
}

function loadHomePage() {
  $('#splash_amai').modal()
}

function getLang() {
  return $('#lang').data('lang') ? 'EN' : 'SP'
}

function getText(key) {
  const lang = getLang()

  const texts = {
    SP: {
      contactFormSuccess: 'Mensaje enviado, Gracias.',
      contactFormError: 'Error, los sentimos, favor de tratar más tarde.'
    },
    EN: {
      contactFormSuccess: 'Email sent, thank you.',
      contactFormError: 'Error, we are sorry, please try later.'
    }
  }

  return texts[lang][key] || ''
}

function getFormData(formSelector) {
  const data = {}
  $.each($(formSelector).serializeArray(), (i, field) => {
    data[field.name] = field.value;
  });
  return data;
}

function loadContactForm() {
  if ($('#contact_form').length) {
    $("#contact_form").validate();

    $('#contact_form').submit(event => {
      if (!$("#contact_form").validate().errorList.length) {
        event.preventDefault()
        $.ajax({
          type: "POST",
          url: '/send_email',
          data: getFormData('#contact_form'),
          success: response => {
            const keyMessage = response && response.status ? 'contactFormSuccess' : 'contactFormError'
            $('#form_response').text(getText(keyMessage))
            $('.custom_submit').hide()
          },
          dataType: 'json'
        });
      }
    })

  }
}

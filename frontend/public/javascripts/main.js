var storage = localStorage.getItem('/aarhus-c/');

$(document).ready(function () {

  $('.button').on('click', function(e) {
    e.preventDefault();
    history.pushState(null, 'Sideskift', '/search/?query=Lyngbyvej+40%2C+2100+København+Ø');
  });

  if( eval($('html').data('appcache')) == true ) {
    $( window.applicationCache ).on( 'updateready', _onUpdateReady );

    // Check to see if anything in the app_cache.manifest has changed
    // We want to check in an interval, in case the user never refreshes
    var timer = setInterval(function() {

      // Checking to see if there is an update, if there is
      // the 'updateready' event is fired.
      window.applicationCache.update();

    }, 180000); // 180000 is 3 Minutes
  }

  if( storage !== null ) {
    getRestaurantListLocal();
  }
  else {
    getRestaurantList();
  }
});

function _onUpdateReady () {
  // When a new update is located, we create a message for the user to see.
  var source = $.get( '/templates/partials/general/update_available.handlebars', function( source ) {
    var template = Handlebars.compile( source );

    var context = { url: window.location.href };
    var html = template( context );

    // We only want to show one message, if multiple updates has been located between client refreshes.
    if( $('.update-available').length == 0 ) {
      $('body').prepend( html );
    }
  });

  // When a new update is located, Swapcache makes sure that 'subsequent' calls to cached resources are taken from the new cache.
  // This means that the next refresh or page_load coming from the user, uses the new files.
  try {
    window.applicationCache.swapCache();
  }
  catch(error) {
    console.log( error.code );
  }
}

function getRestaurantList() {
  var dataUrl = window.location.href + '&async=true';
  var templateUrl = '/templates/restaurant_list.handlebars';
  var dataCollection = {};

  var storage = localStorage.getItem('/aarhus-c/');
  if( storage !== null ) {
    dataUrl = null
    dataCollection['data'] = storage;
  }

  $.when(
    // Get the data
    $.get( dataUrl, function( data ) {
      dataCollection['data'] = data;
      localStorage.setItem('/aarhus-c/', data);
    }),

    // Get the template
    $.get( templateUrl, function( template ) {
      dataCollection['template'] = template;
    })

  ).then(function( data, textStatus, jqXHR ) {
    var template = Handlebars.compile( dataCollection.template );
    var html = template( JSON.parse(dataCollection.data) );

    $('.content').html( html );
  });
}

function getRestaurantListLocal() {
  var dataUrl = window.location.href + '&async=true';
  var templateUrl = '/templates/restaurant_list.handlebars';
  var dataCollection = {};

  dataCollection['data'] = storage;

  $.when(

    // Get the template
    $.get( templateUrl, function( template ) {
      dataCollection['template'] = template;
    })

  ).then(function( data, textStatus, jqXHR ) {
    var template = Handlebars.compile( dataCollection.template );
    var html = template( JSON.parse(dataCollection.data) );

    $('.content').html( html );
  });
}
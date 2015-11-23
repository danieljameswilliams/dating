var App = App || {};

App.Login = (function() {
  'use strict';

  var dom = {};

  function initialize() {
    _setupDOM();
    _addEventListeners();

    loadFacebookScript();
  }

  function _setupDOM() {
    dom.$facebookButton = $('.login__facebook-button');
  }

  function _addEventListeners() {
    dom.$facebookButton.on('click', _onFacebookButtonClicked);
  }

  //////////////
  // Partials //
  //////////////

  function loadFacebookScript() {
    $.ajaxSetup({ cache: true });
    $.getScript('//connect.facebook.net/da_DK/sdk.js', function(){
      FB.init({
        appId: '193820617619307',
        xfbml: true,
        version: 'v2.5'
      });
      dom.$facebookButton.removeAttr('disabled');
      FB.getLoginStatus(checkIfLoggedIn);
    });
  }

  function checkIfLoggedIn( response ) {
    if( response.status == 'connected' ) {
      var userId = response.authResponse.userID;
      var url = 'http://localhost:8000/api/profile/facebook/';

      var formData = {
        'userId': userId
      };

      $.get( url, formData, function( data, textStatus, jqXHR ) {
        if( jqXHR.status == 200 && data !== undefined ) {
          // First we tell the app which user is connected.
          $('body').data('guid', data.guid)
          $('body').data('id', data.id)

          // And then we show the cards, which is the frontpage.
          $('.content').html('<div id="cards"></div>');
          App.Cards.initialize();
        }
      });
    }
  }

  function _onFacebookButtonClicked() {
    FB.login(function( response ){
      checkIfLoggedIn( response );
    }, {
      scope: 'publish_actions, email'
    });
  }

  ////////////////
  // Public API //
  ////////////////

  return {
    initialize: initialize
  };

})();
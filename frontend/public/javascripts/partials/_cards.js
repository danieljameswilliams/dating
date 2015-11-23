var App = App || {};

App.Cards = (function() {
  'use strict';

  var dom = {},
      cardHTML;

  function initialize() {
    loadCardTemplate();

    _setupDOM();
    _addEventListeners();
  }

  function _setupDOM() {
    dom.$cardsWrapper = $('#cards');
  }

  function _addEventListeners() {
    dom.$cardsWrapper.on('click', '.js-answer_button', _onAnswerButtonClicked);
  }


    //////////////
    // Partials //
    //////////////

    function loadCardTemplate() {
      var url = 'templates/partials/card.handlebars';

      $.get( url, function( data ) {
        cardHTML = data;
        getCards();
      });
    }

    function getCards() {
      var url = 'http://localhost:8000/api/cards/1/';

      var formData = {
        'token': $('body').data('guid')
      };

      $.get( url, formData, function( data, textStatus, jqXHR ) {
        if( jqXHR.status == 200 && data !== undefined ) {
          if( typeof(data) == 'string' ) {
            var json = JSON.parse(data);
          }

          for(var i = 0; i < json.cards.length; i++) {
            var isLast = (i == (json.cards.length-1) ? true : false);

            createCard( json.cards[i], isLast );
          }
        }
        else if( jqXHR.status == 204 ) {
          showCardsEmpty();
        }
      });
    }

    function createCard( card, isLast ) {
      var template = Handlebars.compile(cardHTML);
      var user = 'Not Implemented, Yet';

      var context = {
        'card': card,
        'isLast': isLast,
        'user': {
          'token': $('body').data('guid')
        }
      };

      var html = template(context);
      $('#cards').prepend( html );
    }

    function _onAnswerButtonClicked( event ) {
      var card = $(this).parents('.card');
      var cardId = card.data('id');
      var inputValue = card.find('.js-answer_input').val();
      var userId = $('body').data('id');
      var url = 'http://localhost:8000/api/card-answer/' + cardId + '/' + userId + '/';

      var formData = {
        'token': $('body').data('guid'),
        'answer': inputValue
      };

      $.post( url, formData, function( data ) {
        card.remove();
        $('#cards').children().last().addClass('is-active');

        if( dom.$cardsWrapper.children().length == 0 ) {
          showCardsEmpty();
        }
      });
    }

    function showCardsEmpty() {
      var url = 'templates/partials/card--empty.handlebars';

      $.get( url, function( data ) {
        var template = Handlebars.compile( data );
        var html = template({});
        $('#cards').html( html );
      });
    }

    ////////////////
    // Public API //
    ////////////////

    return {
      initialize: initialize
    };

  })();
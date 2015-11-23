var url = require('url');

module.exports = function( request, response ) {
	response.set( 'Content-Type', 'text/html' );

	// Getting all information about the current request.url
	var location = url.parse( request.url, true );

	// Set the context to the page data
	var context = {};

	// Checking if the request has a async query-parameter,
	if( location.query.async ) {
		// We send some JSON to be handled in the frontend.
		response.json( context );
	}
	else {
		// We want to serve some pre-rendered HTML, due to either a server-request or noscript.
		response.render('cards', context);
	}
}
// Adding attributes to the global routes object.

module.exports = function( app, controllers ) {
  return {
    general: require('./partials/general.js')( app, controllers )
  };
};
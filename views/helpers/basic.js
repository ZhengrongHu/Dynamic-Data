const Handlebars = require('handlebars');

Handlebars.registerHelper('bold', function(options){

    var test = new Handlebars.SafeString('<b>' + options.fn(this) + '</b>');

    return test;


});

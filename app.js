'use strict';

const Hapi = require('hapi');
const Blipp = require('blipp');
const Path = require('path');
const Inert = require('inert');
const Vision = require('vision');
const Handlebars = require('handlebars');

const server = new Hapi.Server({

    connections:{

        routes:{
            files:{
                relativeTo: Path.join(__dirname, 'public')
            }
        }
    }

});

server.connection({ port: 4000, host: 'localhost' });

server.register([Blipp, Inert, Vision], ()=> {});

server.views({
    engines: {
        html: Handlebars
    },
    path: 'views',
    layoutPath: 'views/layout',
    layout: 'layout',
    helpersPath: 'views/helpers'


});

server.route({
    method: 'GET',
    path: '/',
    handler:{
        view: {
            template: 'index',
            context:{
                title: 'One Day of Pusheen',
                message: 'How do you feel?',
                pic:'/images/pusheen01.jpg',
                nav: [
                    {
                        url: "/images/pusheen02.jpg",
                        title: "eat",
                       pic:'/images/pusheen02.jpg',
                    },
                    {
                        url: "/images/pusheen03.jpg",
                        title: "draw",
                pic:'/images/pusheen03.jpg'
                    },
                    {
                        url: "images/pusheen04.jpg",
                        title: "sleep",
                pic:'/images/pusheen04.jpg'
                    },

                ],
                menu: [{item: "hello"},{item: "hello"},{item: "hello"}]
            }
        }
    }
});

server.route({
    method: 'GET',
    path: '/{param*}',
    handler:{
        directory:{
            path: './',
            listing: true,
            index: false,
            redirectToSlash: true
        }
    }
});




server.start((err) => {

    if (err) {
        throw err;
    }
    console.log(`Server running at: ${server.info.uri}`);
});

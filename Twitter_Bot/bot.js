
console.log('the bot is starting');

//google trend
/*
const googleTrends = require('google-trends-api');

googleTrends.interestOverTime({keyword: 'Women\'s march'})
.then(function(results){
  console.log('These results are awesome', results);
})
.catch(function(err){
  console.error('Oh no there was an error', err);
});
*/

//emoji 


var Twit = require('twit');

var config = require('./config'); // go up to directory and look for config
var T = new Twit(config);
//get 
var params = {
    q: '‪‪Dave Chappelle', 
    count: 50
}

T.get('search/tweets', params, gotData);

function gotData(err, data, response){
    var tweets = data.statuses;
    for (var i =0; i < tweets.length; i ++){
        console.log(tweets[i].text);
    }
}

var EmojiData = require('emoji-data');
 
    EmojiData.scan("I ♥ ♥♥♥♥ talking about the Pusheens").forEach(
        function(ec) { console.log("Found some " + ec.short_name + "!");
                     }
        );
                      
//Streaming API

var stream = T.stream('user');

stream.on('follow', followed);

function followed(eventMsg){
    var name = eventMsg.source.name;
    var screenName = eventMsg.source.screen_name;
    tweetIt('@' + screenName + 'why are you followin me?');
}


//get 
/*
var params = {
    q: 'chinita', 
    count: 50
}

T.get('search/tweets', params, gotData);

function gotData(err, data, response){
    var tweets = data.statuses;
    for (var i =0; i < tweets.length; i ++){
        console.log(tweets[i].text);
    }
};
*/

//post
setInterval(tweetIt, 10000*20)

tweetIt();


function tweetIt(){
    var r = Math.floor(Math.random()*100);
    var tweet = {
        status: '#Chinita is trying to figure out emoji' + r + 'times',
    }

    T.post('statuses/update', tweet, tweeted);

    function tweeted (err, data, response) {
        if (err) {
            console.log("Errors");
        }else {
            console.log("Works");
        }
        }
        }
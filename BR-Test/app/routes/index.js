var express = require('express');
var router = express.Router();

router.get('/', function(req, res) {
  var data = req.app.get('appData');
  var pagePhotos = [];
  var pageStudents = data.students;

  data.students.forEach(function(item) {
    pagePhotos = pagePhotos.concat(item.weapons);
  });

  res.render('index', {
    pageTitle: 'Home',
    weapons: pagePhotos,
    students: pageStudents,
    pageID: 'home'
  });

});

module.exports = router;

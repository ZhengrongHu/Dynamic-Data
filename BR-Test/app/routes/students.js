var express = require('express');
var router = express.Router();

router.get('/students', function(req, res) {
  var data = req.app.get('appData');
  var pagePhotos = [];
  var pageStudents = data.students;

  data.students.forEach(function(item) {
    pagePhotos = pagePhotos.concat(item.wepaons);
  });

  res.render('students', {
    pageTitle: 'Students',
    wepaons: pagePhotos,
    students: pageStudents,
    pageID: 'studentList'
  });
});

router.get('/students/:speakerid', function(req, res) {
  var data = req.app.get('appData');
  var pagePhotos = [];
  var pageStudents = [];

  data.students.forEach(function(item) {
    if (item.shortname == req.params.speakerid) {
      pageStudents.push(item);
      pagePhotos = pagePhotos.concat(item.wepaons);
    }
  });

  res.render('students', {
    pageTitle: 'Students Info',
    wepaons: pagePhotos,
    students: pageStudents,
    pageID: 'studentDetail'
  });
});

module.exports = router;

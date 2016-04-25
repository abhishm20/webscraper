var mysql = require('mysql')
var pyshell = require('./pyshell')

var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'ainaa',
    database: 'webscraper'
})

connection.connect(function(err) {
    if (err) throw err

    connection.query('Select * from alertbot_alert;', function(err, alerts){
        if(err) throw err;
        var alert;
        for (alert of alerts) {
            pyshell('flipkart', alert.url, function(err, res){

            })
        }
    })
})

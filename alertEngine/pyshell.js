var PythonShell = require('python-shell');

var options = {
  mode: 'text',
  scriptPath: './',
  pythonOptions: ['-u'],
  args: ['asd']
};

var pyshell = new PythonShell('flipkart.py');

pyshell.on('message', function (message) {
// received a message sent from the Python script (a simple "print" statement)
console.log(message); });
pyshell.send('hello');
module.exports = function(scriptType, url, cb){
    console.log(url);
    pyshell.send(url);
    PythonShell.run('flipkart.py', options, function (err, results) {
      if (err) throw err;
      // results is an array consisting of messages collected during execution
      console.log('results: %j', results);
    });

}

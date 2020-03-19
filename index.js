const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http);

io.on('connection', function(socket){
  socket.on('update list', function(task){
      io.emit('update list', task)
  })
});

http.listen(2000, function(){
  console.log('listening on *:2000');
});


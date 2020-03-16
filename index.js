const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http);

io.on('connection', function(socket){
    console.log('someone joined')
  io.on('new user', function(){
      console.log('new user joined')
  })
});

http.listen(2000, function(){
  console.log('listening on *:2000');
});
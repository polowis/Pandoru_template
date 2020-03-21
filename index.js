const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const redisAdapter = require('socket.io-redis');
io.adapter(redisAdapter({ host: 'localhost', port: 6379 }));

io.on('connection', function(socket){
  socket.on('update list', function(data){
      io.in(data.room).emit('update list', data.task)
      //io.emit('update list', task)
  })
  socket.on('privateroom', (room) => {
    socket.join(room)
  })
});

http.listen(2000, function(){
  console.log('listening on *:2000');
});


const urlParameters = getUrlParameters();
const room = urlParameters.room;
const player = urlParameters.player;

const websocket = new WebSocket("ws://127.0.0.1:5000");

const exit = function() {
  const message = {
    room: room,
    player: player,
    action: { type: "exit" }
  }
  websocket.send(JSON.stringify(message));
  window.location.href = 'index.html';
}

const enter = function() {
  const message = {
    room: room,
    player: player,
    action: { type: "enter" }
  }
  websocket.send(JSON.stringify(message));
}

$(document).ready(function() {
  $("#exit_button").click(exit);
  websocket.onopen = function(event) {
    enter(room, player)
  };
  websocket.onmessage = function(event) {
    // app.users.push({ name: 'New Player' })
    const json = JSON.parse(event.data);
    switch (json.action) {
      case 'enter':
      case 'exit':
        app.players = json.players
        console.log(event.data);
        break;
    }
  }

  const app = new Vue({
    el: '#player_list',
    data: {
      players: []
    }
  })
});
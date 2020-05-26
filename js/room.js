const urlParameters = getUrlParameters();
const room = urlParameters.room;
const player = urlParameters.player;

const websocket = new WebSocket("ws://127.0.0.1:5000");
let app;
let players;

const enter = function() {
  const message = {
    room: room,
    player: player,
    action: { type: "enter" }
  }
  websocket.send(JSON.stringify(message));
}

const exit = function() {
  const message = {
    room: room,
    player: player,
    action: { type: "exit" }
  }
  websocket.send(JSON.stringify(message));
  window.location.href = 'index.html';
}

const game_start = function() {
  const message = {
    room: room,
    player: player,
    action: { type: "start" }
  }
  websocket.send(JSON.stringify(message));
}

const down = function() {
  let card_num = $("#input_num").val();
  const message = {
    room: room,
    player: player,
    action: {
      type: "down",
      card: card_num
    }
  }
  websocket.send(JSON.stringify(message));
}

const bid = function() {
  let declared_number = $("#input_num").val();
  const message = {
    room: room,
    player: player,
    action: { type: "bid", num: declared_number }
  }
  websocket.send(JSON.stringify(message));
}

const reveal = function() {
  let target_player_num = $("#input_num").val();
  let target_player = players[target_player_num].name;
  const message = {
    room: room,
    player: player,
    action: {
      type: "reveal",
      player: target_player
    }
  }
  websocket.send(JSON.stringify(message));
}

const pass = function() {
  const message = {
    room: room,
    player: player,
    action: { type: "pass" }
  }
  websocket.send(JSON.stringify(message));
}

const on_message = function(event) {
  // app.users.push({ name: 'New Player' })
  const json = JSON.parse(event.data);
  switch (json.action) {
    case 'start':
    case 'enter':
    case 'exit':
      app.players = json.players
      console.log(event.data);
      break;
    case 'down':
    case 'bid':
    case 'pass':
    case 'reveal':
      console.log(event.data);
      break;
  }
}

$(document).ready(function() {
  $("#exit_button").click(exit);
  $("#start_button").click(game_start);
  $("#down_button").click(down);
  $("#bid_button").click(bid);
  $("#pass_button").click(pass);
  $("#reveal_button").click(reveal);

  app = new Vue({
    el: '#player_list',
    data: {
      game: {},
      players: []
    }
  });
  players = app.players;

  websocket.onopen = function(event) {
    enter(room, player)
  };
  websocket.onmessage = on_message;
});
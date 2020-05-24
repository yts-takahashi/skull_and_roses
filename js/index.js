enter = function() {
  const room = $("#room_name").val();
  const player = $("#player_name").val();
  window.location.href = `room.html?player=${player}&room=${room}`;
}
$(document).ready(function() {
  $("#enter_button").click(enter);
});
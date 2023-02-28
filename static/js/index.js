const roomName = JSON.parse(document.getElementById('room-name').textContent);
const username = JSON.parse(document.getElementById('username').textContent);
const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/rooms/' + roomName + '/');


// Send message to the server
document.querySelector('#chat-message-submit').onclick = function (e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    chatSocket.send(JSON.stringify({
        'username': username,
        'message': message
    }));
    messageInputDom.value = '';
};

// Receive message from the server
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    const message = data['message'];
    const username_data = data['username'];

    let messagesBox = document.querySelector('.box-messages');
    let new_message = '';
    if (username === username_data) {
        new_message = `<p class="my-message">${username_data}: ${message}</p>`;
    } else {
        new_message = `<p class="others-message">${username_data}: ${message}</p>`;
    }
    messagesBox.innerHTML += new_message;
}
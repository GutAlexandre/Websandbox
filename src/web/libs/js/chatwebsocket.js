
var pseudo = prompt("Entrez votre nom", "");
document.title = "Chat with Websocket : " + pseudo;
var chatBox = document.getElementById('chat-box');
var ws = new WebSocket(`ws://localhost:8000/ws/${pseudo}`);

ws.onmessage = function (event) {
    var message = event.data;
    console.log(event)
    appendMessage(message, true);
};

function change(e) {
    if (e.value == "None") {
        document.getElementById('messageText').disabled = true;
    } else {
        document.getElementById('messageText').disabled = false;
    }
}

function toggleButtonState() {
    const messageText = document.getElementById('messageText');
    const sendButton = document.getElementById('sendButton');
    if (messageText.value.trim() === '') {
        sendButton.disabled = true;
    } else {
        sendButton.disabled = false;
    }
}

function sendMessage() {
    const sendButton = document.getElementById('sendButton');
    sendButton.disabled = true;
    var message = document.getElementById("messageText").value;

    const select = document.getElementById("websocket-select");
    let id = select.selectedIndex - 1;
    const options = select.options;
    if (id === options.length - 2) {
        id = "Broadcast"
    }
    const data = new URLSearchParams();
    data.append("message", message);
    data.append("id", id);
    data.append("who", pseudo);
    appendMessage(message, false);
    ws.send(data)

    document.getElementById("messageText").value = '';
}

function appendMessage(message, isResponse) {
    var messageElement = document.createElement('p');
    messageElement.className = isResponse ? 'text-success' : 'text-primary';
    messageElement.textContent = isResponse ?  message : pseudo + ': ' + message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; 
}

function displayConnections(connections) {
    var websocketSelect = document.getElementById("websocket-select");
    websocketSelect.innerHTML = "";
    var option = document.createElement("option");
    option.value = "None";
    option.textContent = "Sélectionnez une WebSocket"
    websocketSelect.appendChild(option);

    if (connections && Array.isArray(connections.connections)) {
        connections.connections.forEach(function (connection, index) {
            var option = document.createElement("option");
            option.value = connection;
            option.textContent = "Connection " + index + ": " + connection;
            websocketSelect.appendChild(option);
        });
        var option = document.createElement("option");
        option.value = "Broadcast";
        option.textContent = "Broadcast"
        websocketSelect.appendChild(option);
    } else {
        console.error("Les connexions ne sont pas au format attendu.");
    }

}

function getWebSocketConnections() {
    fetch("http://localhost:8000/get_connections")
        .then(response => response.json())
        .then(data => {
            displayConnections(data.connections);
        });
}





getWebSocketConnections()
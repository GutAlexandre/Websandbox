const serial = new Serial();
var chatBox = document.getElementById('chat-box');

serial.on(SerialEvents.CONNECTION_OPENED, onSerialConnectionOpened);
serial.on(SerialEvents.CONNECTION_CLOSED, onSerialConnectionClosed);
serial.on(SerialEvents.DATA_RECEIVED, onSerialDataReceived);
serial.on(SerialEvents.ERROR_OCCURRED, onSerialErrorOccurred);

function onSerialErrorOccurred(eventSender, error) {
    console.log("onSerialErrorOccurred", error);
}

function onSerialConnectionOpened(eventSender) {
    console.log("onSerialConnectionOpened", eventSender);
    document.getElementById('messageText').disabled = false;
}

function onSerialConnectionClosed(eventSender) {
    console.log("onSerialConnectionClosed", eventSender);
}

function onSerialDataReceived(eventSender, newData) {
    console.log("onSerialDataReceived", newData);
    appendMessage( newData, true);
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

function appendMessage(message, isResponse) {
    const maintenant = new Date();

    const heures = maintenant.getHours();
    const minutes = maintenant.getMinutes();
    const secondes = maintenant.getSeconds();
    const heureMinuteSeconde = `${heures}:${minutes}:${secondes}`;
    
    var messageElement = document.createElement('p');
    messageElement.className = isResponse ? 'text-success' : 'text-primary';
    messageElement.textContent = heureMinuteSeconde + ' : ' + message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; 
}

async function onConnectButtonClick() {
    
    if (navigator.serial) {
        if (!serial.isOpen()) {
            await serial.connectAndOpen(null, { baudRate: 115200});
        } else {
            console.log("The serial connection appears already open");
        }
    } else {
        alert('The Web Serial API does not appear supported on this web browser.');
    }

}

async function onSend(text) {
    console.log("Writing to serial:", text);
    serial.writeLine(text);
}


document.getElementById('sendButton').addEventListener('click', sendMessage);

async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const message = userInput.value.trim();
    if (message) {
        displayMessage(message, 'user');
        userInput.value = '';

        try {
            const response = await fetch('/api/message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();
            displayMessage(data.reply, 'bot');
        } catch (error) {
            console.error('Error al enviar el mensaje:', error);
            displayMessage('Hubo un error. Por favor intenta nuevamente.', 'bot');
        }
    }
}

function displayMessage(message, sender) {
    const chatbox = document.getElementById('chatbox');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.textContent = message;
    chatbox.appendChild(messageElement);
    chatbox.scrollTop = chatbox.scrollHeight;
}

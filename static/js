

let question = document.getElementById("chat-input");
    question.addEventListener("keypress", function(event) {

        if (event.key === "Enter") {

            event.preventDefault();

            extractText();

        }


});



function extractText() {

    let user_question = document.getElementById("chat-input").value;

    document.getElementById("chat-input").value = "";

    response(user_question);

    let chat_container = document.getElementById("list-group");

    const user_container = document.createElement("div");
    user_container.setAttribute('id', 'user');
    chat_container.append(user_container);

    // Change Image to user's profile picture
    const user_image = document.createElement("img");
    user_image.setAttribute("id", "user_avatar");
    user_image.setAttribute("src", "/static/images/user.PNG");
    user_container.append(user_image);

    const user_text = document.createElement("p");
    user_text.innerText = user_question;
    user_container.append(user_text);

};

function response(prompt) {

    prompt = prompt.replace('/', "%2F");

    let user_prompt = {
        
        'type' : 'POST',
        'prompt': prompt

    };


    const request = new XMLHttpRequest();
    const encodedPrompt = encodeURIComponent(JSON.stringify(user_prompt));  // Encode the prompt
    
    request.open('POST', `/processUserInfo/${encodedPrompt}`);
    request.onload = () => {

        try {

            const bot_response = request.responseText;

            renderBotResponse(bot_response);
            
        } catch (error) {
            
            console.error(error);

        }

    }

    request.send();

};

function renderBotResponse (bot_response) {

    let response = bot_response;

    let chat_container = document.getElementById("list-group");

    const bot_container = document.createElement("div");
    bot_container.setAttribute('id', 'bot');
    chat_container.append(bot_container);

    const bot_image = document.createElement("img");
    bot_image.setAttribute("id", "bot_avatar");
    bot_image.setAttribute("src", "/static/images/bot.PNG");
    bot_container.append(bot_image);

    const bot_text = document.createElement("p");
    bot_text.innerText = response;
    bot_container.append(bot_text);


};







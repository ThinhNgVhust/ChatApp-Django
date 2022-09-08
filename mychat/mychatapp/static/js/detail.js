document.addEventListener("DOMContentLoaded",function(){

    let form = document.getElementById("myform");

    // https://docs.djangoproject.com/en/4.1/howto/csrf/
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');
    form.addEventListener("submit",sendChat);

    function sendChat(event)
    {
        //get value and send to the backend
        let chatMessage= document.getElementById("id_body").value
        console.log(chatMessage)

        const data = { msg: chatMessage };
        const profileId = document.querySelector("img").id
        console.log("id ",profileId)
        let url = `sent_msg/${profileId}`;

        fetch(url, {
            method: 'POST', // or 'PUT'
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(data),
          })
          .then(response => response.json())
          .then(data => {
            console.log('Success:', data);
            let chat_body = document.getElementById('chat-body')
            let chatMessageBox = document.createElement("div")
            chatMessageBox.classList.add("chat-box-sent")
            chatMessageBox.innerText = data
            chat_body.append(chatMessageBox)
            document.getElementById("id_body").value=""
          })
          .catch((error) => {
            console.error('Error:', error);
          });
        event.preventDefault();
        
    }

});
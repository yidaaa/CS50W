document.addEventListener("DOMContentLoaded", function () {
  // Use buttons to toggle between views
  document.querySelector("#inbox").addEventListener("click", () => load_mailbox("inbox"));
  document.querySelector("#sent").addEventListener("click", () => load_mailbox("sent"));
  document.querySelector("#archived").addEventListener("click", () => load_mailbox("archive"));
  document.querySelector("#compose").addEventListener("click", () => compose_email(false, []));
  load_mailbox("inbox");
});

function compose_email(reply, arr) {
  // Show compose view and hide other views
  document.querySelector("#emails-view").style.display = "none";
  document.querySelector("#email-view").style.display = "none";
  document.querySelector("#compose-view").style.display = "block";
  
  if (reply){
    document.querySelector("#compose-recipients").value = arr[0];
    document.querySelector("#compose-subject").value = arr[1];
    document.querySelector("#compose-body").value = arr[2];
  } else {
    // Clear out composition fields
    document.querySelector("#compose-recipients").value = "";
    document.querySelector("#compose-subject").value = "";
    document.querySelector("#compose-body").value = "";
  }

  // Send an email
  document.querySelector("#compose-form").onsubmit = () => {
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: document.querySelector("#compose-recipients").value,
          subject: document.querySelector("#compose-subject").value,
          body: document.querySelector("#compose-body").value,
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log(result);
    })
    .catch((error) => {
        console.error(error);
      });
    
    setTimeout(() => load_mailbox("sent"), 800);
    return false;
  };
}

function load_mailbox(mailbox) {
  // Show the mailbox and hide other views
  document.querySelector("#emails-view").style.display = "block";
  document.querySelector("#email-view").style.display = "none";
  document.querySelector("#compose-view").style.display = "none";
  document.querySelector("#emails-view").innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    emails.forEach(email => {
      email_block = document.createElement('div');

      email_block.style.border = "thin solid black";
      if (email["read"]){
        email_block.style.backgroundColor = "gray";
      } else {
        email_block.style.backgroundColor = "white";
      }
      
      email_block.innerHTML = `
        <div id="email_timestamp">${email["timestamp"]}</div>
        <div id="email_sender">${email["sender"]}</div>
        <div id="email_subject">${email["subject"]}</div>
      `;

      // open email wrt ID 
      email_block.onclick = () => {
        read(email.id, true);
        load_email(email.id);
      }

      document.querySelector('#emails-view').append(email_block);
    }); 
  });
}

function load_email(id) {
  fetch(`/emails/${id}`)
    .then((response) => response.json())
    .then((email) => {
      email_view = document.querySelector("#email-view");
      email_view.style.display = "block";
      document.querySelector("#emails-view").style.display = "none";
      document.querySelector("#compose-view").style.display = "none";
      
      // change email-view content
      email_view.innerHTML = `
        <div> <div class="title"> From: </div> ${email["sender"]} </div> 
        <div> <div class="title"> To: </div> ${email["recipients"]} </div> 
        <div> <div class="title"> Subject: </div> ${email["subject"]} </div> 
        <div> <div class="title"> Timestamp: </div> ${email["timestamp"]} </div> 
        <div id="non-title">${email["body"]}</div>
        <br>`;

      if (!email["archived"]){
        email_view.insertAdjacentHTML('beforeend', `
          <div class="buttons"> 
          <button id="reply">Reply</button>
          <button id="archive">Archive</button>
          </div>`
        );
        //archive email
        document.querySelector("#archive").onclick = () => {
          archive(id, true);
          location.reload();
        };
      } else {
        email_view.insertAdjacentHTML('beforeend', `
          <div class="buttons"> 
          <button id="reply">Reply</button>
          <button id="unarchive">Unarchive</button>
          </div>`
        );
        //unarchive email
        document.querySelector("#unarchive").onclick = () => {
          archive(id, false);
          location.reload();
        };
      }

      document.querySelector("#reply").onclick = () => {
        to = email["sender"];
        subject = email["subject"];
        if (subject.slice(0,3) !== "Re:"){
          subject = "Re: " + subject; 
        }
        text = `On ${email["timestamp"]}, ${to} wrote: ${email["body"]}`;

        arr = [to, subject, text];
        compose_email(true, arr);
      };

    })
    .catch((error) => {
      console.error(error);
    });
}

function read(id, boolean) {
  // id = email id, boolean = {true, false}
  fetch(`/emails/${id}`, {
    method: "PUT",
    body: JSON.stringify({
      read: boolean,
    }),
  });
}

function archive(id, boolean) {
  // id = email id, boolean = {true, false}
  fetch(`/emails/${id}`, {
    method: "PUT",
    body: JSON.stringify({
      archived: boolean,
    }),
  });
}

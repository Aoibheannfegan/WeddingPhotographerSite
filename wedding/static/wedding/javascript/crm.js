document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#event').addEventListener('click', () => load_event());
    document.querySelector('#notes').addEventListener('click', () => load_notes());
    document.querySelector('#approve-button').addEventListener('click', () => approve());
  
    // By default, load event
    load_event();
});

  
function load_event() {
  
    // Show event view and hide notes view
    document.querySelector('#event-view').style.display = 'block';
    document.querySelector('#note-view').style.display = 'none';

    const eventBtn = document.getElementById('event');
    const noteBtn = document.getElementById('notes');

    // Reset both buttons to default
    eventBtn.classList.remove('btn-secondary');
    noteBtn.classList.remove('btn-secondary');
    eventBtn.classList.add('btn-outline-secondary');
    noteBtn.classList.add('btn-outline-secondary');

    // Set active button
    eventBtn.classList.add('btn-secondary');
    eventBtn.classList.remove('btn-outline-secondary');
}
  
function load_notes() {
    document.querySelector('#note-view').style.display = 'block';
    document.querySelector('#event-view').style.display = 'none';

    const eventBtn = document.getElementById('event');
    const noteBtn = document.getElementById('notes');
    
    // Reset both buttons to default
    eventBtn.classList.remove('btn-secondary');
    noteBtn.classList.remove('btn-secondary');
    eventBtn.classList.add('btn-outline-secondary');
    noteBtn.classList.add('btn-outline-secondary');

    // Set active button
    noteBtn.classList.add('btn-secondary');
    noteBtn.classList.remove('btn-outline-secondary');
}

function approve() {
    const btn = document.getElementById('approve-button');
    console.log("btn:", btn);

    const clientId = btn.getAttribute('data-client-id');
    console.log("clientId:", clientId);

    action = 'success'
    console.log(action)

    const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value
    console.log(csrfToken)

    fetch(`/approve_request/${clientId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken  // Add this line
        },
        body: JSON.stringify({
            action: action
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            btn.innerHTML = "Approved"
        } else {
            alert('Something went wrong. Please try again later')
        }
    });
}
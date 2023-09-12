
document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    fetch('/api/unavailable_dates/')
    .then(response => response.json())
    .then(data => {
        var calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            events: data,
            dateClick: function(info) {
                addEvent(info,calendar);
            },
            eventClick: function(info) {
                viewEvent(info, calendar);
            }
        });
        calendar.render();
    });
  });

function addEvent(info, calendar) {
    console.log('add Event function running')
    document.querySelector('#view-event').style.display = 'none';
    document.querySelector('#book-event').style.display = 'block';

    var dateClicked = info.dateStr; // date clicked in 'YYYY-MM-DD' format
    document.querySelector('#book-event [name="date"]').value = dateClicked;
    var dateElement = document.getElementById('current-date');
    dateElement.innerHTML = "Date: " + dateClicked;
    calendar.updateSize(); 

    document.querySelector('#create-event').addEventListener('click', (e) => {
        var titleInput = document.querySelector('#book-event [name="title"]').value;
        // Validate the title input
        if(titleInput.trim() === '') {
            alert("Please enter a title for the event.");
            e.preventDefault();
        } else {
            var event = {
                title: titleInput,
                start: dateClicked,
            };

            calendar.addEvent(event);
            document.querySelector('#book-event').style.display = 'none';
        }
    });

    document.querySelector('#close-book').addEventListener('click', () => {
        document.querySelector('#book-event').style.display = 'none';
        calendar.updateSize();
    });
}

function viewEvent(info, calendar) {
    console.log('view Event function running')
    //make event details visible
    document.querySelector('#book-event').style.display = 'none';
    document.querySelector('#view-event').style.display = 'block';
    calendar.updateSize();

    var eventClickedId = info.event.id;
    console.log(eventClickedId)
    //query the db for details of clicked event
    fetch(`/api/event_details/${eventClickedId}/`)
    .then(response => response.json())
    .then(data => {
        // display appropriate event details
        document.querySelector('#view-event .title').textContent = "Title: " + data.title;
        document.querySelector('#view-event .description').textContent = "Description: " + data.description;
        document.querySelector('#view-event .date').textContent = "Date: " + data.date;
    });

    //when close button clicked hide the event details view again
    document.querySelector('#close-event').addEventListener('click', () => {
        document.querySelector('#view-event').style.display = 'none';
        calendar.updateSize();
    });
}

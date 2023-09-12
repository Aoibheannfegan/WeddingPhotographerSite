document.addEventListener('DOMContentLoaded', function() {    
    const editButtons = document.querySelectorAll('.editBtn');
    editButtons.forEach(button => {
        button.addEventListener('click', editPackage);
    });
});

function getFetchHeaders() {
    const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    return {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
    };
}

function editPackage() {
    console.log("edit function called");

    const editBtn = event.currentTarget;

    //get post id
    const packageId = editBtn.getAttribute('data-package-id');

    const elements = {
        descriptionElem: document.querySelector(`.description[data-package-id="${packageId}"]`),
        titleElem: document.querySelector(`.title[data-package-id="${packageId}"]`),
        priceElem: document.querySelector(`.price[data-package-id="${packageId}"]`),
        deetsElem: document.querySelector(`.deets[data-package-id="${packageId}"]`)
    };

    Object.values(elements).forEach(elem => elem.style.display = 'none');

    //replace elememts with text area 
    const textareas = {
        description: document.createElement('textarea'),
        title: document.createElement('textarea'),
        price: document.createElement('textarea'),
        deets: document.createElement('textarea')
    };

    fetch(`/api/package_details/${packageId}/`)
    .then(response => response.json())
    .then(data => {
        //prepopulate textareas with relevant values
        textareas.description.value = data.description;
        textareas.title.value = data.title;
        textareas.price.value = data.price;
        textareas.deets.value = data.deets;
    
        elements.descriptionElem.after(textareas.description);
        elements.titleElem.after(textareas.title);
        elements.priceElem.after(textareas.price);
        elements.deetsElem.after(textareas.deets);

         //create a save button
        const saveButton = document.createElement('button');
        saveButton.className = 'btn btn-info';
        saveButton.textContent = "Save";
        textareas.deets.after(saveButton);

        //run save action when save is clicked
        saveButton.onclick = function() {
            const updatedValues = {
                description: textareas.description.value,
                title: textareas.title.value,
                price: textareas.price.value,
                deets: textareas.deets.value
            };

            const headers = getFetchHeaders();
            fetch(`/edit/${packageId}/`, {
                method: 'POST',
                body: JSON.stringify(updatedValues),
                headers: headers
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // show updated content
                    elements.descriptionElem.innerHTML = data.description;
                    elements.titleElem.innerHTML = data.title;
                    elements.priceElem.innerHTML = data.price;
                    elements.deetsElem.innerHTML = data.deets;

                    // Restore visibility and remove textareas
                    Object.values(elements).forEach(elem => elem.style.display = 'block');
                    Object.values(textareas).forEach(textarea => textarea.remove());
                    
                    saveButton.remove();  
                } else {
                    alert('Something went wrong. Please try again later')
                }
            });
        };
    });
}
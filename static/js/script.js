/* Confirm script.js connected */
console.log('script.js connected')

/* Star Rating System */
function rateSession(element) {
    var value = parseInt(element.getAttribute('data-value'));
    var stars = element.querySelectorAll('.fa-star');
    for (var i = 0; i < stars.length; i++) {
        if (i < value) {
            stars[i].classList.add('checked');
        } else {
            stars[i].classList.remove('checked');
        }
    }
    
    // Send AJAX request to update rating
    var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    fetch('/update_rating/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ 'rating': value }),
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Failed to update rating');
        }
    })
    .then(data => {
        console.log(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
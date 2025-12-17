const form = document.getElementById('reviewForm');
const reviewsContainer = document.getElementById('reviews');


async function loadReviews() {
    const response = await fetch('/reviews');
    const reviews = await response.json();
    
    reviewsContainer.innerHTML = '';
    reviews.reverse().forEach(review => {
        const item = document.createElement("p");
        item.textContent = `Review from ${review.name}: ${review.review}`;
        reviewsContainer.appendChild(item);
    });
}

form.addEventListener("submit", async (event) => {

    event.preventDefault()
    
    const name = form.elements.name.value;
    const review = form.elements.review.value;

    //const item = document.createElement("p");
    
    //item.textContent = `Review from ${name}: ${review}`;
    //reviewsContainer.appendChild(item);

    //form.reset();

    await fetch('/reviews', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, review })
    });

    form.reset();
    await loadReviews(); 
});

loadReviews();

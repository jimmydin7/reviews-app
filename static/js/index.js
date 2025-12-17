const form = document.getElementById('reviewForm');
const reviewsContainer = document.getElementById('reviews');

form.addEventListener("submit", (event) => {

    event.preventDefault()
    
    const name = form.elements.name.value;
    const review = form.elements.review.value;

    const item = document.createElement("p");
    
    item.textContent = `Review from ${name}: ${review}`;
    reviewsContainer.appendChild(item);

    form.reset();

})



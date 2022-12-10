const toggleBtn = document.querySelectorAll('.toggle-btn');

toggleBtn.forEach(btn => {
    btn.addEventListener('click', () => {
        btn.parentNode.classList.toggle('active')  //only toggles the parent node which is the '.faq-card' here
    })
})
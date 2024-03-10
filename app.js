const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) =>{
        console.log(entry)
        if (entry.isIntersecting) {
            entry.target.classList.add('recipe-show');
        } else {
            entry.target.classList.remove('recipe-show');
        }
    });
});

const hiddenElements = document.querySelector('.recipe');
hiddenElements.forEach((el) => observer.observe(el));
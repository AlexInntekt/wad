const togglebutton = document.getElementsByClassName('mytoggle')[0];
const navbarlinks = document.getElementsByClassName('mylinks')[0];

togglebutton.addEventListener('click', () => {
    navbarlinks.classList.toggle('active');
});
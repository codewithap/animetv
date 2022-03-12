let Sinp = document.querySelector('#searchInp');
let Sform = document.querySelector('form');
let navBar = document.querySelector('#nav-bar');
let navBarSection = document.querySelector('#nav-bar-section');
let navOpen = document.querySelector('#navopen');
Sinp.addEventListener('input', () => {
    if (Sinp.value == '') {
        Sform.action = '#';
    } else {
        Sform.action = `/search?query=${Sinp.value}`;
    }
});
navBarSection.style.display = 'none';

function navopen() {
    navBar.style.transition = '0.3s';
    navBar.style.width = '50vw';
    navBarSection.style.display = 'block';
    navOpen.style.opacity = '0.1';
}

function closeNav() {
    navBar.style.transition = '0.3s';
    navBar.style.width = '0px';
    navBarSection.style.display = 'none';
    navOpen.style.opacity = '1';
}
let navBar = document.querySelector('#nav-bar');
let navBarSection = document.querySelector('#nav-bar-section');
let navOpen = document.querySelector('#navopen');
let search = document.querySelector('#search');
let searchForm = document.querySelector('#searchForm');
sBtn = document.querySelector('#sBtn');
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

search.addEventListener('input', () => {
    searchForm.action = `/search?query=${search.value}`;
});
search.style.height = '0';
sBtn.addEventListener('click', () => {
    if (search.type == 'hidden') {
        search.type = 'text';
        search.style.height = '2.5rem';
    }
    else {
        search.type = 'hidden';
        search.style.height = '0';
    }
});

let arr = []
if (sessionStorage.getItem('ids') == null) {
    sessionStorage.setItem('ids', '[]')
} else if (sessionStorage.getItem('ids') != null) {
    b = JSON.parse(sessionStorage.getItem('ids'));
    for (let i = 0; i < b.length; i++) {
        arr.push(b[i]);
    }
}

function save(e) {
    activeBtn(e)
    ids = sessionStorage.getItem('ids')
    if (ids.includes(e) == true) {
        a = 'alrady added';
    }
    else {
        arr.push(e)
        strArr = JSON.stringify(arr)
        sessionStorage.setItem('ids', strArr)
    }
    console.log(sessionStorage.getItem('ids'))
}

function activeBtn(btn) {
    x = document.querySelector(`#${btn}`);
    x.setAttribute('style', `
            color: skyblue;
            background: #252632;
            `);
}
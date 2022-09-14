const navBtn = document.getElementById('userPerfil');

function toggleMenu (){
    const nav = document.getElementById('nav_opcoes')
    nav.classList.toggle(active)
}

navBtn.addEventListener('click',toggleMenu)
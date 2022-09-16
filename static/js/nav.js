const navBtn = document.getElementById('userPerfil');

function toggleMenu (){
    const nav = document.getElementById('nav_opcoes')
    nav.classList.toggle(active)
    console.log("teste")
}

navBtn.addEventListener('click',toggleMenu)
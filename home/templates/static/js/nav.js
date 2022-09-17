const navBtn = document.getElementById('userPerfil');
console.log("teste")

function toggleMenu (){
    const nav = document.getElementById('nav_opcoes')
    nav.classList.toggle("active")
    console.log("teste")
}

navBtn.addEventListener('click',toggleMenu)
/*=============== MOSTRAR MENÚ ===============*/

const navMenu = document.getElementById('nav-menu'),
      navToggleMenu = document.getElementById('nav-toggle-menu'),
      navCloseMenu = document.getElementById('nav-close-menu');
      
      /*=============== MOSTRAR CARRITO ===============*/
      
const navShop = document.getElementById('nav-shop'),    
      navToggleShop = document.getElementById('nav-toggle-shop'),
      navCloseShop = document.getElementById('nav-close-shop');

/* Validar si existe la constante */

if (navToggleMenu) {
    navToggleMenu.addEventListener('click', () => {
    navMenu.classList.add('show-menu');
  });
}

if (navToggleShop) {
    navToggleShop.addEventListener('click', () => {
      navShop.classList.add('show-shop');
    });
  }

/* Ocultar Menú */

if (navCloseMenu) {
    navCloseMenu.addEventListener('click', () => {
      navMenu.classList.remove('show-menu');
    });
  }

if (navCloseShop) {
    navCloseShop.addEventListener('click', () => {
    navShop.classList.remove('show-shop');
  });
}

/*=============== REMUEVE EL MENÚ EN MOVIL ===============*/

const navLinks = document.querySelectorAll('.nav__link');

function linkAction () {

    const navMenu = document.getElementById('nav-menu');
    /* Cuando demos click en cada nav__link, se remueve el show-menu */
    navMenu.classList.remove('show-menu');

}

navLinks.forEach( n => n.addEventListener('click', linkAction));

/*=============== CAMBIAR BACKGROUND DEL HEADER ===============*/

function scrollHeader () {

    const header = document.getElementById('header');
    // Cuando el scroll sea mayor a 80vh, añadir la clase scroll-header al header
    if (this.scrollY >= 80) {
        header.classList.add('scroll-header');
    } else {
        header.classList.remove('scroll-header');
    }
}

window.addEventListener('scroll', scrollHeader);

/*=============== QUESTIONS ACCORDION ===============*/

const accordionItems = document.querySelectorAll('.questions__item');

accordionItems.forEach( item => {

    const accordionHeader = item.querySelector('.questions__header');

    accordionHeader.addEventListener('click', () => {

        const openItem = document.querySelector('.accordion-open');

        toggleItem(item);

        if (openItem && openItem !== item) {
            toggleItem(openItem);
        } 

    });
})

const toggleItem = (item) => {

    const accordionContent = item.querySelector('.questions__content');

    if (item.classList.contains('accordion-open')) {
        item.classList.remove('accordion-open');
        accordionContent.removeAttribute('style');
    } else {

        accordionContent.style.height = accordionContent.scrollHeight + 'px';
        item.classList.add('accordion-open');

    }
}

/*=============== SCROLL SECCIONES DE UN ENLACE ACTIVO ===============*/

const sections = document.querySelectorAll('section');
const navLi    = document.querySelectorAll('nav .nav__menu ul li');

window.addEventListener('scroll', () => { 

    let current = '';

    sections.forEach( section => {

        const sectionTop    = section.offsetTop;
        const sectionHeight = section.clientHeight;

        /* if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) { */
        if (scrollY >= (sectionTop - sectionHeight / 3)) {
            current = section.getAttribute('id');
        }
        
    });
    
    navLi.forEach( li => {

        li.classList.remove('active-link');

        if (li.classList.contains(current)) {
            li.classList.add('active-link');
        }

    });
    
});

/* const nav_link = document.querySelectorAll('.nav__item a');

function scrollActivate () {

    var URLactual = window.location.href;
    var url = URLactual.split('#');
    var url = url[1];
    /* console.log(URLactual);
    console.log(url); 

    nav_link.forEach( link => {

        
        
            
        if (link.getAttribute('href') === '#' + url ) {
            link.classList.add('active-link');
            
        } else {
            if (link.classList.contains('nav__link')) {
                link.classList.remove('active-link');
            }
        }
        

    });

}

window.addEventListener('scroll', scrollActivate); */

/*=============== MOSTRAR SCROLL UP ===============*/ 

function scrollUp () {

    const scrollUp = document.getElementById('scroll-up');

    /* Cuando el scroll es mayor a 200vh de altura, se añade la clase show-scroll */
    if (this.scrollY >= 200) scrollUp.classList.add('show-scroll'); else scrollUp.classList.remove('show-scroll');

}

window.addEventListener('scroll', scrollUp);

/*=============== DARK LIGHT THEME ===============*/ 

const btnTheme  = document.getElementById('btn-theme');
const darkTheme = 'dark-theme';
const iconTheme = 'ri-sun-line';

/* Almacenamos el tema previo (Si el usuario lo seleccionó) */
const selectedTheme = localStorage.getItem('selected-theme');
const selectedIcon  = localStorage.getItem('selected-icon');

/* Obtenemos el tema actual de la interfaz validando la clase dark-theme */
const getCurrentTheme = () => document.body.classList.contains(darkTheme) ? 'dark' : 'light';
const getCurrentIcon  = () => btnTheme.classList.contains(iconTheme) ? 'ri-moon-line' : 'ri-sun-line';

/* Validamos si el usuario eligió un tema previamente */
if (selectedTheme) {
    document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme);
    btnTheme.classList[selectedIcon === 'ri-moon-line' ? 'add' : 'remove'](iconTheme);
}

/* Activar y desactivar el dark mode Manualmente */
btnTheme.addEventListener('click', () => {

    /* Añadir o remover el icono */
    document.body.classList.toggle(darkTheme);
    btnTheme.classList.toggle(iconTheme);

    /* Almacenamos el tema y el icono actual que el usuario eligió */
    localStorage.setItem('selected-theme', getCurrentTheme());
    localStorage.setItem('selected-icon' , getCurrentIcon());

});

/*=============== ANIMACIÓN SCROLL REVEAL ===============*/

const sr = ScrollReveal({

    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 400,
    // reset: true

});

sr.reveal(`.home__data`);
sr.reveal(`.home__img`, { delay: 500 });
sr.reveal(`.home__social`, { delay: 600 });
sr.reveal(`.about__img, .contact__box`, { origin: 'left' });
sr.reveal(`.about__data, .contact__form`, { origin: 'right' });
sr.reveal(`.steps__card, .product__card, .questions__group, .extra`, { interval: 100 });

/*=============== ANIMACIÓN DEL LOADER ===============*/

function loaderContainer () {
    
    document.querySelector('.section__loader').classList.add('hidden');
    
}

function loader () {
    
    setInterval(loaderContainer, 3000);
    
}

window.onload = loader;
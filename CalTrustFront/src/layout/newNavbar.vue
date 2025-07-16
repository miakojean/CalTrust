<template>
  <nav class="nav" :class="{ 'nav--fixed-scrolled': isFixed, 'nav--visible': isVisible }">
    <div class="nav__logo">
      <h3>Caltrust</h3>
    </div>

    <ul class="nav__links" :class="{ 'nav__links--open': isMenuOpen }">
      <li><a href="#">Accueil</a></li>
      <li><a href="#">Entreprises</a></li>
      <li><a href="#">Avis</a></li>
      <li><a href="#">À propos</a></li>
      <li><a href="#">Contact</a></li>
    </ul>

    <div class="nav__btn">
      <hamburger 
        :is-active="isMenuOpen" 
        @toggle="toggleMenu" 
        aria-controls="nav-menu"
      />
    </div>

    <div class="auth__btn">
      <secondButton/>
      <mainButton label = "connexion"/>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import hamburger from '@/components/button/hamburger.vue';
import secondButton from '@/components/button/secondButton.vue';
import mainButton from '@/components/button/mainButton.vue';

const isMenuOpen = ref(false);
const isFixed = ref(false);
const isVisible = ref(false);
const isDesktop = ref(window.innerWidth >= 768); // Nouvelle référence pour le mode desktop
const scrollThreshold = 50;
let lastScrollY = window.scrollY;

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

const handleScroll = () => {
  // Ne pas appliquer le scroll effect sur mobile
  if (!isDesktop.value) {
    isFixed.value = false;
    isVisible.value = true;
    return;
  }

  const currentScrollY = window.scrollY;
  
  if (currentScrollY <= scrollThreshold || isMenuOpen.value) {
    isVisible.value = true;
    isFixed.value = currentScrollY > scrollThreshold;
    lastScrollY = currentScrollY;
    return;
  }

  const scrollingDown = currentScrollY > lastScrollY;
  
  isFixed.value = true;
  isVisible.value = !scrollingDown;
  
  lastScrollY = currentScrollY;
};

const handleResize = () => {
  isDesktop.value = window.innerWidth >= 768;
  // Réinitialiser l'état de la navbar lors du changement de taille
  if (!isDesktop.value) {
    isFixed.value = false;
    isVisible.value = true;
  }
};

onMounted(() => {
  isVisible.value = true;
  window.addEventListener('scroll', handleScroll, { passive: true });
  window.addEventListener('resize', handleResize);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
  window.removeEventListener('resize', handleResize);
});
</script>

<style scoped>
.nav {
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  z-index: 1000;
  /* Transition seulement sur desktop */
  transition: transform 0.4s ease-in-out, background-color 0.4s ease;
  transform: translateY(0);
}

/* Ces styles ne s'appliquent que sur desktop */
@media (min-width: 768px) {
  .nav--fixed-scrolled {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: white;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    transform: translateY(-100%);
  }

  .nav--fixed-scrolled.nav--visible {
    transform: translateY(0);
  }
}

/* Le reste de votre CSS reste inchangé */
.nav__links {
  position: fixed;
  top: 0;
  left: -10%;
  width: 100%;
  height: 100vh;
  background: #f3f3f3;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  transform: translateX(-100%);
  transition: transform 0.3s ease-in-out;
  z-index: 90;
  margin: 0;
  padding: 0;
  font-size: 0.9rem;
}

.nav__links--open {
  transform: translateX(0);
}

.nav__btn {
  z-index: 100;
}

.auth__btn {
  display: none;
}

@media (min-width: 890px) {
  nav {
    display: flex;
    justify-content: space-around;
  }

  .nav__links {
    position: static;
    flex-direction: row;
    height: auto;
    width: auto;
    background: transparent;
    transform: none !important;
  }
  
  .nav__btn {
    display: none;
  }

  .auth__btn {
    width: auto;
    display: flex;
    justify-content: space-around;
    align-items: center;
    gap: 1rem;
  }
}
</style>
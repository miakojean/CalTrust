<template>
  <nav class="nav" :class="{ 'nav--fixed-scrolled': isFixed, 'nav--visible': isVisible }">
    <div class="nav__logo">
      <h3>Caltrust</h3>
    </div>

    <ul class="nav__links" :class="{ 'nav__links--open': isMenuOpen }">
      <li><a href="#">accueil</a></li>
      <li><a href="#">entreprises</a></li>
      <li><a href="#">avis</a></li>
      <li><a href="#">à propos</a></li>
      <li><a href="#">contact</a></li>
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
const scrollThreshold = 50; // Pixels to scroll before the navbar becomes fixed
let lastScrollY = window.scrollY;

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};

const handleScroll = () => {
  const currentScrollY = window.scrollY;
  
  // Toujours visible en haut de page ou si le menu est ouvert
  if (currentScrollY <= scrollThreshold || isMenuOpen.value) {
    isVisible.value = true;
    isFixed.value = currentScrollY > scrollThreshold;
    lastScrollY.value = currentScrollY;
    return;
  }

  // Détermine la direction du scroll
  const scrollingDown = currentScrollY > lastScrollY.value;
  
  isFixed.value = true;
  isVisible.value = !scrollingDown;
  
  lastScrollY.value = currentScrollY;
};

// Add and remove the scroll event listener
onMounted(() => {
  isVisible.value = true; // Ensure navbar is visible on initial load
  window.addEventListener('scroll', handleScroll, { passive: true });
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
.nav {
  position: relative;
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 1rem;
  z-index: 1000;
  /* Add transition for smooth effect */
  transition: transform 0.4s ease-in-out, background-color 0.4s ease;
  transform: translateY(0); /* Start visible */
}

/* This class applies when the user has scrolled past the threshold */
.nav--fixed-scrolled {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: white; /* Or your desired background */
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  /* Initially hide the navbar when it becomes fixed and user is scrolling down */
  transform: translateY(-100%); 
}

/* This class makes the fixed navbar slide into view */
.nav--fixed-scrolled.nav--visible {
  transform: translateY(0);
}

.nav__links {
  position: fixed;
  top: 0;
  left: 0;
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

/* --- Desktop Styles --- */
@media (min-width: 768px) {
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

/* Redundant media query removed for clarity, as 768px covers it */
</style>
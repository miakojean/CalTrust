<template>
  <nav class="nav__container" :class="{ 'scrolled': isScrolled }">
    <div class="div__logo">
      <h3><router-link to="/">CalTrust</router-link></h3>
    </div>
    
    <!-- Bouton Hamburger -->
    <button 
      class="hamburger"
      :class="{ active: isMenuOpen }"
      @click="toggleMenu"
      aria-label="Menu"
      :aria-expanded="isMenuOpen"
    >
      <span class="hamburger__line"></span>
      <span class="hamburger__line"></span>
      <span class="hamburger__line"></span>
    </button>
    
    <!-- Menu Navigation -->
    <div 
      class="div__menu"
      :class="{ active: isMenuOpen }"
    >
      <ul @click="closeMenu">
        <li v-for="link in navLinks" :key="link.path">
          <router-link 
            :to="link.path"
            :class="{ active: isActive(link) }"
          >
            {{ link.name }}
          </router-link>
        </li>
      </ul>
    </div>

    <div class="btn__started">
      <startButton label="Commencer" @click="navigateToServices"/>
    </div>
  </nav>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

export default {
  name: 'Navbar',
  setup() {
    const route = useRoute();
    const router = useRouter();
    const isMenuOpen = ref(false);
    const isScrolled = ref(false);

    const navLinks = [
      { path: '/', name: 'Accueil', exact: true },
      { path: '/about', name: 'A propos' },
      { path: '/services', name: 'Services' },
      { path: '/contact', name: 'Contact' },
      { path: '/newsletter', name: 'Newsletter' },
    ];

    const isActive = (link) => {
      if (link.exact) {
        return route.path === link.path;
      }
      return route.path.startsWith(link.path);
    };

    const toggleMenu = () => {
      isMenuOpen.value = !isMenuOpen.value;
    };

    const closeMenu = () => {
      isMenuOpen.value = false;
    };

    const navigateToServices = () => {
      closeMenu();
      router.push('/quote');
    };

    const handleScroll = () => {
      isScrolled.value = window.scrollY > 10;
    };

    onMounted(() => {
      window.addEventListener('scroll', handleScroll);
    });

    onUnmounted(() => {
      window.removeEventListener('scroll', handleScroll);
    });

    return {
      isMenuOpen,
      isScrolled,
      navLinks,
      isActive,
      toggleMenu,
      closeMenu,
      navigateToServices
    };
  }
};
</script>

<style scoped>
.nav__container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: transparent;
  transition: all 0.5s ease;
  color: #111;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.nav__container.scrolled {
  background-color: #252525f8;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
}

.div__logo h3 {
  font-weight: 500;
  font-size: 1.5rem;
  color: #111;
  margin: 0;
  transition: transform 0.3s ease;
}

.div__logo h3:hover {
  transform: scale(1.05);
}

.div__logo a {
  color: inherit;
  text-decoration: none;
}

.div__menu ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.div__menu li {
  margin-left: 2rem;
}

.div__menu a {
  text-decoration: none;
  color: #111;
  font-weight: 400;
  transition: all 0.3s ease;
  position: relative;
  padding: 0.5rem 0;
}

.div__menu a:hover {
  color: #4dabf7;
}

.div__menu a.active {
  color: #4dabf7;
  font-weight: 500;
}

.div__menu a.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: #4dabf7;
  transform: scaleX(1);
  transform-origin: left;
  transition: transform 0.3s ease;
}

/* Bouton Hamburger */
.hamburger {
  display: none;
  cursor: pointer;
  background: transparent;
  border: none;
  padding: 0.5rem;
  z-index: 1001;
}

.hamburger__line {
  display: block;
  width: 25px;
  height: 3px;
  background-color: #111;
  margin: 5px 0;
  transition: all 0.3s ease;
  border-radius: 3px;
}

/* Responsive Design */
@media (max-width: 1150px) {
  .nav__container {
    padding: 1rem;
  }

  .hamburger {
    display: block;
  }

  .div__menu {
    position: fixed;
    top: 70px;
    left: 0;
    width: 100%;
    height: calc(100vh - 70px);
    background-color: #f3f3f3;
    backdrop-filter: blur(10px);
    padding: 2rem 1rem;
    transform: translateX(-100%);
    transition: transform 0.3s ease;
    z-index: 1000;
    overflow-y: auto;
  }

  .div__menu.active {
    transform: translateX(0);
  }

  .div__menu ul {
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
  }

  .div__menu li {
    margin: 0;
    width: 100%;
    text-align: center;
  }

  .div__menu a {
    display: block;
    padding: 1rem;
    font-size: 1.2rem;
  }

  /* Animation Hamburger */
  .hamburger.active .hamburger__line:nth-child(1) {
    transform: translateY(8px) rotate(45deg);
  }

  .hamburger.active .hamburger__line:nth-child(2) {
    opacity: 0;
  }

  .hamburger.active .hamburger__line:nth-child(3) {
    transform: translateY(-8px) rotate(-45deg);
  }

  .btn__started {
    display: none;
  }
}

/* Animation du menu mobile */
@media (max-width: 768px) {
  .div__menu {
    top: 60px;
    height: calc(100vh - 60px);
  }
}
</style>
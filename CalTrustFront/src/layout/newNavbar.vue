<template>
  <nav class="navbar" :class="{ scrolled: isScrolled }">
    <div class="logo">
      <router-link to="/">CalTrust</router-link>
    </div>
    
    <button 
      class="menu-toggle"
      @click="toggleMenu"
      :aria-expanded="isMenuOpen"
    >
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </button>
    
    <div class="nav-links" :class="{ active: isMenuOpen }">
      <router-link 
        v-for="link in links"
        :key="link.path"
        :to="link.path"
        @click="closeMenu"
        :class="{ active: isActive(link) }"
      >
        {{ link.name }}
      </router-link>
      
      <div class="auth-buttons">
        <button @click="navigateTo('/login')" class="btn-login">Connexion</button>
        <button @click="navigateTo('/register')" class="btn-register">Inscription</button>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();
const isMenuOpen = ref(false);
const isScrolled = ref(false);

const links = [
  { path: '/', name: 'Accueil', exact: true },
  { path: '/avis', name: 'Avis' },
  { path: '/about', name: 'À propos' },
  { path: '/entreprises', name: 'Entreprises' }
];

const isActive = (link) => {
  return link.exact ? route.path === link.path : route.path.startsWith(link.path);
};

const toggleMenu = () => isMenuOpen.value = !isMenuOpen.value;
const closeMenu = () => isMenuOpen.value = false;
const navigateTo = (path) => {
  closeMenu();
  router.push(path);
};

const handleScroll = () => {
  isScrolled.value = window.scrollY > 10;
};

onMounted(() => window.addEventListener('scroll', handleScroll));
onUnmounted(() => window.removeEventListener('scroll', handleScroll));
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
}

.navbar.scrolled {
  background: rgba(0, 0, 0, 0.9);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.logo a {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1B3C53;
  text-decoration: none;
}

.navbar.scrolled .logo a {
  color: white;
}

.menu-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
}

.bar {
  display: block;
  width: 25px;
  height: 3px;
  margin: 5px 0;
  background: #1B3C53;
  transition: all 0.3s ease;
}

.navbar.scrolled .bar {
  background: white;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.nav-links a {
  color: #333;
  text-decoration: none;
  font-weight: 500;
  padding: 0.5rem 0;
  position: relative;
}

.nav-links a.active {
  color: #2F6B8E;
  font-weight: 600;
}

.nav-links a.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: #2F6B8E;
}

.navbar.scrolled .nav-links a {
  color: white;
}

.navbar.scrolled .nav-links a.active {
  color: #4A8CAF;
}

.auth-buttons {
  display: flex;
  gap: 1rem;
  margin-left: 1rem;
}

.btn-login, .btn-register {
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-login {
  background: transparent;
  border: 1px solid #2F6B8E;
  color: #2F6B8E;
}

.btn-register {
  background: #2F6B8E;
  border: 1px solid #2F6B8E;
  color: white;
}

.navbar.scrolled .btn-login {
  border-color: white;
  color: white;
}

.navbar.scrolled .btn-register {
  background: white;
  color: #1B3C53;
  border-color: white;
}

@media (min-width: 768px) {
  .menu-toggle {
    display: block;
    z-index: 1001;
  }

  .menu-toggle.active .bar:nth-child(1) {
    transform: translateY(8px) rotate(45deg);
  }

  .menu-toggle.active .bar:nth-child(2) {
    opacity: 0;
  }

  .menu-toggle.active .bar:nth-child(3) {
    transform: translateY(-8px) rotate(-45deg);
  }

  .nav-links {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    flex-direction: column;
    justify-content: center;
    transform: translateX(-100%);
    transition: transform 0.3s ease;
    gap: 2rem;
  }

  .nav-links.active {
    transform: translateX(0);
  }

  .auth-buttons {
    flex-direction: column;
    margin-left: 0;
    width: 200px;
  }

  .navbar.scrolled .nav-links {
    background: rgba(0, 0, 0, 0.95);
  }
}
</style>
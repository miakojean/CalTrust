<template>
  <nav class="nav" :class="{ 'nav--fixed-scrolled': isFixed, 'nav--visible': isVisible }">
    <div class="nav__logo">
      <h3>Caltrust</h3>
    </div>

    <ul class="nav__links" :class="{ 'nav__links--open': isMenuOpen }">
      <li><router-link to="/">Accueil</router-link></li>
      <li><router-link to="/avis">Avis</router-link></li>
      <li><a href="#">À propos</a></li>
      <li><a href="#">Contact</a></li>
      <li><a href="#">Entreprises</a></li>
    </ul>

    <div class="nav__btn">
      <hamburger 
        :is-active="isMenuOpen" 
        @toggle="toggleMenu" 
        aria-controls="nav-menu"
      />
    </div>

    <div class="auth__btn" v-if="isLoggedIn === false">
      <secondButton/>
      <mainButton @click="login" label = "Connexion"/>
    </div>

    <div class="auth__btn" v-if="isLoggedIn === true">
      <secondButton :label = "username"/>
      <mainButton label = "Deconnexion" @click="logout"/>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import hamburger from '@/components/button/hamburger.vue';
import secondButton from '@/components/button/secondButton.vue';
import mainButton from '@/components/button/mainButton.vue';
import api from '@/_services/_authservices';
import { useRouter } from 'vue-router';

const isLoggedIn = ref(false);

const isMenuOpen = ref(false);
const isFixed = ref(false);
const isVisible = ref(false);
const isDesktop = ref(window.innerWidth >= 768); // Nouvelle référence pour le mode desktop
const scrollThreshold = 50;
let lastScrollY = window.scrollY;
const router = useRouter();

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};
const login = () => {
  router.push('/signin'); // Redirection vers la page de connexion
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

const username = ref('')

const isAuthenticated = () =>{
  if (localStorage.getItem('userToken') && localStorage.getItem('userTokenRefresh')){
    username.value = localStorage.getItem('username')
    isLoggedIn.value = true
    return true
  } else 
    return false
}

const logout = async () => {
  // Récupérer les deux tokens depuis le localStorage
  const accessToken = localStorage.getItem('userToken');
  const refreshToken = localStorage.getItem('userTokenRefresh'); // Assurez-vous que c'est la bonne clé

  // Si l'un des tokens manque, on nettoie et on arrête
  if (!refreshToken || !accessToken) {
    console.error("Tokens manquants pour la déconnexion.");
    localStorage.clear(); // Nettoyage par sécurité
    // Mettez à jour votre UI ici (ex: isLoggedIn.value = false)
    return;
  }

  try {
    // 1. Préparer le corps (body) de la requête avec le refresh token
    const requestBody = {
      refresh: refreshToken,
    };

    // 2. Préparer les en-têtes (headers) avec l'access token
    const requestConfig = {
      headers: {
        'Authorization': `Bearer ${accessToken}`
      }
    };

    // 3. Envoyer la requête POST avec l'URL, le corps et les en-têtes
    await api.post('/account/logout/', requestBody, requestConfig);
    router.push('/signin')
    
    console.log("Déconnexion réussie côté serveur.");

  } catch (error) {
    console.error("Échec de la déconnexion côté serveur:", error.response ? error.response.data : error.message);
    // Même en cas d'erreur (ex: token expiré), il faut déconnecter l'utilisateur côté client.
  } finally {
    // 4. Quoi qu'il arrive, nettoyer le localStorage pour finaliser la déconnexion côté client
    localStorage.removeItem('userToken');
    localStorage.removeItem('userTokenRefresh');
    localStorage.removeItem('username'); // N'oubliez pas le nom d'utilisateur

    // Mettez à jour l'état de votre application (ex: isLoggedIn.value = false)
    // et redirigez l'utilisateur si nécessaire.
  }
  router.push('/signin');
};

onMounted(() => {
  isVisible.value = true;
  window.addEventListener('scroll', handleScroll, { passive: true });
  window.addEventListener('resize', handleResize);
  isAuthenticated()
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
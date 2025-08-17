<template>
  <main>
    <newNavbar/>
    <div class="settings__view">
      <div class="settings-menu-container">
        <settingsMenu/>
      </div>
      <div class="profile-settings-container">
        <profileSecuritySection/>
      </div>
    </div>
    <footerSection/>
  </main>
</template>

<script>
import newNavbar from '@/layout/newNavbar.vue';
import settingsMenu from '../settingsMenu.vue';
import profileSecuritySection from '../profileSection/profileSecuritySection.vue';
import footerSection from '@/layout/footerSection.vue';

export default {
  components: {
    newNavbar,
    settingsMenu,
    profileSecuritySection,
    footerSection
  }
}
</script>

<style scoped>
.settings__view {
  display: flex;
  min-height: calc(100vh - 120px); /* Ajustez selon la hauteur de votre navbar/footer */
}

.settings-menu-container {
  position: sticky;
  top: 80px; /* Ajustez selon la hauteur de votre navbar */
  height: fit-content;
  align-self: flex-start;
  width: 250px; /* Largeur fixe pour le menu */
  flex-shrink: 0;
}

.profile-settings-container {
  flex-grow: 1;
  padding: 1rem;
  max-width: calc(100% - 250px); /* Largeur totale moins le menu */
}

/* Pour les écrans plus petits */
@media (max-width: 768px) {
  .settings__view {
    flex-direction: column;
  }
  
  .settings-menu-container {
    position: static;
    width: 100%;
  }
  
  .profile-settings-container {
    max-width: 100%;
  }
}
</style>
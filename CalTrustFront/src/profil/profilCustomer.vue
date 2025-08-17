<template>
  <main>
    <newNavbar/>
    <div class="settings__view">
      <settingsMenu/>
      <profileSettings/>
    </div>
    <footerSection/>
  </main>
</template>

<script>
import newNavbar from '@/layout/newNavbar.vue';
import settingsMenu from './profileComponents/settingsMenu.vue';
import profileSettings from './profileComponents/profileSettings.vue';
import footerSection from '@/layout/footerSection.vue';
export default {

  components:{
    newNavbar,
    settingsMenu,
    profileSettings,
    footerSection
  }

}
</script>

<style scoped>
.settings__view{
  display:flex;
  gap: 1rem;
}
</style>
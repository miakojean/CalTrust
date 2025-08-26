<template>
  <div class="main__container">
    <h3>Details de l'avis</h3>
    <notifCard />
  </div>
</template>

<script>
import testimonialCardForFirm from '@/components/cards/testimonialCardForFirm.vue';
import notifCard from '@/components/notifications/notifCard.vue';
export default {
  components: {
    testimonialCardForFirm,
    notifCard
  }
}
</script>

<style scoped>

</style>
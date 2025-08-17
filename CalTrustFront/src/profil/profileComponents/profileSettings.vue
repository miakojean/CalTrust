<template>
  <section class="profile__section">
    <profileInfoBlock/>
    <profileInfoBlock/>
    <profileInfoBlock/>
  </section>
</template>

<script>
import profileInfoBlock from './profileInfoBlock.vue';
export default {
    components:{
        profileInfoBlock,
    }
}
</script>

<style scoped>
.profile__section{
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}
</style>
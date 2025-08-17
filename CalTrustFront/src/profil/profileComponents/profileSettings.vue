<template>
  <section class="profile__section">
    <profileInfoBlock
      :isThereDescription="false"
      :isThereToggle="false"
    />
    <profileInfoBlock
      title="Informations supplémentaires"
      description="Ici vous retrouvez vos informations supplémentaires"
      :fields="otherFields"
    />
  </section>
</template>

<script>
import { ref } from 'vue';
import profileInfoBlock from './profileInfoBlock.vue';
export default {
  components:{
    profileInfoBlock,
  },

  setup(){
    const otherFields = ref([
      { label: 'Catégorie', value: "Services Financiers & Banques" },
      { label: 'website', value: "www.firms.com" },
      {label:'Mise en ligne', value:"12/02/2025"}
    ])

    return{
      otherFields,
    }
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
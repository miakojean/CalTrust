<template>
  <button class="main__button" :style="{ width: width }" :disabled="isLoading">
    <template v-if="isLoading">
      <loader aria-label="Chargement"/>
    </template>
    <template v-else>
      {{ label }}
      <i class="fa-solid fa-arrow-up-right-from-square"></i>
    </template>
  </button>
</template>

<script>
import loader from '../tools/loader.vue';
export default {
  props: {
    label: { type: String, default: 'voir l\'entreprise' },
    isLoading: { type: Boolean, default: false },
    width: {
            type: String,
            default: 'auto'
        }
  },
  components: { loader }
};
</script>

<style scoped>

.main__button{
    background: #f3f3f3;
    color: var(--primary-color);
    transition: 0.5s;
    border-radius: 2rem;
    width: 50%;
    max-width: 200px;
    font-size: 0.65rem;
    font-weight: 400;
    transition: ease-in-out 0.3s;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0.5rem;
}

.main__button:hover{
    background: #d3d3d3;
    transition: ease-in-out 0.3s;
}

.main__button i{
    font-size: 0.5rem;
}

@media(min-width: 1024px){
  .main__button{
    font-size: 0.8rem;
  }
}
</style>
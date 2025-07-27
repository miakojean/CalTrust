<template>
  <button class="main__button" :style="{ width: width }" :disabled="isLoading">
    <template v-if="isLoading">
      <loader aria-label="Chargement"/>
    </template>
    <template v-else>
      {{ label }}
    </template>
  </button>
</template>

<script>
import loader from '../tools/loader.vue';
export default {
  props: {
    label: { type: String, default: 'Poster un avis' },
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
    background: var(--primary-color);
    color: white;
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
}

.main__button:hover{
    background: var(--secondary-color);
    transition: ease-in-out 0.3s;
}
</style>
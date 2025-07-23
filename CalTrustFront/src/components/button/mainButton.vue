<template>
  <button class="main__button" :disabled="isLoading">
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
    label: { type: String, default: 'Get Started' },
    isLoading: { type: Boolean, default: false }
  },
  components: { loader }
};
</script>

<style scoped>
.main__button{
    background: var(--primary-color);
    color: #fff;
    transition: 0.5s;
    border-radius: 2rem;
    width: 100%;
    max-width: 600px;
}

.main__button:hover{
    background: #1e5179;
    transition: ease-in-out 0.3s;
}
</style>
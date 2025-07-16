<template>
  <div class="checkbox__comp flex__center">
    <label 
      for="consumer" 
      class="checkbox__family" 
      :class="{ 'selected': selectedOption === 'consumer' }"
    >
      <input 
        type="radio" 
        name="userType" 
        id="consumer" 
        value="consumer"
        v-model="selectedOption"
      >
      <span><i class="fa-solid fa-person"></i></span>
      <div class="label">
        <h4 class="label__">
          {{ labelOne }}
        </h4>
        <p class="sub__label">{{ description }}</p>
      </div>
    </label>

    <label 
      for="company" 
      class="checkbox__family" 
      :class="{ 'selected': selectedOption === 'company' }"
    >
      <input 
        type="radio" 
        name="userType" 
        id="company" 
        value="company"
        v-model="selectedOption"
      >
      <span><i class="fa-solid fa-building"></i></span>
      <div class="label">
        <h4 class="label__">
          {{ labelTwo }}
        </h4>
        <p class="sub__label">{{ descriptionTwo }}</p>
      </div>
    </label>
  </div>
</template>

<script>
import { ref, watch } from 'vue';

export default {
  props: {
    labelOne: {
      type: String,
      default: "Je suis un consommateur"
    },
    labelTwo: {
      type: String,
      default: "Je suis une entreprise"
    },
    description: {
      type: String,
      default: "Compte utilisateur juste pour des avis"
    },
    descriptionTwo: {
      type: String,
      default: "Compte business pour collecter des avis avec plus de features"
    }
  },
  emits: ['selection-changed'], // Bonne pratique : déclarer les événements émis
  
  setup(props, { emit }) {
    // 1. On crée une variable réactive pour stocker la sélection
    // 'consumer' est la valeur par défaut.
    const selectedOption = ref('consumer');

    // 2. On observe les changements de la variable pour émettre un événement
    watch(selectedOption, (newValue) => {
      emit('selection-changed', newValue);
    });

    // 3. On retourne les variables et fonctions qu'on veut rendre accessibles au template
    return {
      selectedOption
    };
  }
}
</script>

<style scoped>


.checkbox__family{
  padding: 1rem 0;
  background: #f8f8f8;
  display: flex;
  justify-content: start;
  align-items: center;
  border-radius: 0.5rem;
  gap: 1rem;
  border: 2px solid transparent;
  transition: ease-in-out 0.8s;
}

.checkbox__family.selected {
  border: 2px solid #2f4b66; /* La couleur de votre bordure */
  background: #f0f4f8; /* Optionnel : changer aussi le fond */
  transition: ease-in-out 0.5s;
}

input{
  width: 15%;
  height: 15%;
}

.label__{
  font-size: 0.9rem;
  color: #2f4b66;
}

.sub__label{
  font-size: 0.8rem;
}

span{
  background: #2f4b66;
  display: center;
  justify-content: center;
  border-radius: 1rem;
  padding: 0.6rem;
}

i{
  background: none;
  font-size: 1.5rem;
  color: #f3f3f3;
}
</style>
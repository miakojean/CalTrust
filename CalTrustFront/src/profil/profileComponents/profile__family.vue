<template>
  <div class="profile__family">
    <div class="label__family">
      <label>{{ label }}</label>
      <p v-if="!isChanging">{{ value }}</p>
      <input v-else type="text" :value="value" class="family-input">
    </div>
    <span class="update-btn" @click="modify">{{ isChanging ? 'Save' : 'Update' }}</span>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  props: {
    label: {
      type: String,
      default: 'Nom de famille'
    },
    value: {
      type: String,
      default: 'Tim Cook'
    },
  },
  setup() {
    const isChanging = ref(false);
    
    const modify = () => {
      isChanging.value = !isChanging.value;
    };

    return {
      isChanging,
      modify,
    };
  }
};
</script>

<style scoped>
.profile__family {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  margin-bottom: 1rem;
}

.label__family {
  display: flex;
  align-items: center;
  flex-grow: 1;
  gap: 1rem;
}

label {
  color: var(--my-black-color);
  font-size: 0.9rem;
  min-width: 120px; /* Largeur fixe pour les labels */
  text-align: left;
}

p, .family-input {
  font-size: 0.9rem;
  flex-grow: 1;
  margin: 0;
}

.family-input {
  padding: 0.3rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.update-btn {
  font-weight: 500;
  color: var(--primary-color);
  cursor: pointer;
  margin-left: 1rem;
  min-width: 60px;
  text-align: right;
}

.update-btn:hover {
  text-decoration: underline;
}
</style>
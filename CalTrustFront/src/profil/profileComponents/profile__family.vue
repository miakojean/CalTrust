<template>
  <div class="profile__family-wrapper">
    <div class="profile__family">
      <div class="label__family">
        <label>{{ label }}</label>
        <p v-if="!isChanging">{{ value }}</p>
        <input v-else type="text" :value="value" class="family-input">
      </div>
      <span class="update-btn" @click="modify">{{ isChanging ? 'Enregistrer' : 'Mettre à jour' }}</span>
    </div>
    <div class="divider"></div>
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
.profile__family-wrapper {
  width: 100%;
  margin-bottom: 0.5rem;
}

.profile__family {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding-bottom: 0.8rem;
}

.label__family {
  display: flex;
  align-items: center;
  flex-grow: 1;
  gap: 2rem;
}

label {
  color: var(--my-black-color);
  font-size: 0.9rem;
  min-width: 120px;
  text-align: left;
}

p, .family-input {
  font-size: 0.9rem;
  flex-grow: 1;
  margin: 0;
  text-align: start;
}

span{
    font-size: 0.9rem;
}

.family-input {
  padding: 0.3rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  width: 100%;
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

.divider {
  height: 1px;
  background-color: #e0e0e0;
  width: 100%;
}
</style>
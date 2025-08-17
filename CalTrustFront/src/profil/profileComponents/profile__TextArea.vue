<template>
  <div class="profile__description-wrapper">
    <div class="profile__description">
      <div class="label__description">
        <label>{{ label }}</label>
        <p v-if="!isChanging">{{ value }}</p>
        <textarea v-else :value="value" class="description-textarea" rows="4"></textarea>
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
      default: 'Description'
    },
    value: {
      type: String,
      default: ''
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
.profile__description-wrapper {
  width: 100%;
  margin-bottom: 0.5rem;
}

.profile__description {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  width: 100%;
  padding-bottom: 0.8rem;
}

.label__description {
  display: flex;
  align-items: flex-start;
  flex-grow: 1;
  gap: 2rem;
}

label {
  color: var(--my-black-color);
  font-size: 0.9rem;
  min-width: 120px;
  text-align: left;
}

p, .description-textarea {
  font-size: 0.9rem;
  flex-grow: 1;
  margin: 0;
  text-align: start;
}

span {
  font-size: 0.9rem;
}

.description-textarea {
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  width: 100%;
  resize: vertical;
  font-family: inherit;
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
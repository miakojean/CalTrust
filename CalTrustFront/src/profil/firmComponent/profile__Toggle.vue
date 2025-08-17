<template>
  <div class="profile__toggle-wrapper">
    <div class="profile__toggle">
      <div class="label__toggle">
        <label>{{ label }}</label>
        <p v-if="!isChanging">{{ value ? activeText : inactiveText }}</p>
        <div v-else class="toggle-container">
          <button 
            class="toggle-option" 
            :class="{ 'active': value }"
            @click="toggleValue(true)"
          >
            {{ activeText }}
          </button>
          <button 
            class="toggle-option" 
            :class="{ 'active': !value }"
            @click="toggleValue(false)"
          >
            {{ inactiveText }}
          </button>
        </div>
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
      default: 'Statut'
    },
    value: {
      type: Boolean,
      default: false
    },
    activeText: {
      type: String,
      default: 'Vérifié'
    },
    inactiveText: {
      type: String,
      default: 'Non vérifié'
    }
  },
  setup(props, { emit }) {
    const isChanging = ref(false);
    const localValue = ref(props.value);
    
    const modify = () => {
      if (isChanging.value) {
        emit('update:value', localValue.value);
      }
      isChanging.value = !isChanging.value;
    };

    const toggleValue = (newValue) => {
      localValue.value = newValue;
    };

    return {
      isChanging,
      localValue,
      modify,
      toggleValue
    };
  }
};
</script>

<style scoped>
.profile__toggle-wrapper {
  width: 100%;
  margin-bottom: 0.5rem;
}

.profile__toggle {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding-bottom: 0.8rem;
}

.label__toggle {
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

p {
  font-size: 0.9rem;
  flex-grow: 1;
  margin: 0;
  text-align: start;
}

span {
  font-size: 0.9rem;
}

.toggle-container {
  display: flex;
  gap: 0.5rem;
}

.toggle-option {
  padding: 0.3rem 0.8rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f5f5f5;
  cursor: pointer;
  transition: all 0.2s;
}

.toggle-option.active {
  background-color: var(--primary-color);
  color: white;
  border-color: var(--primary-color);
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
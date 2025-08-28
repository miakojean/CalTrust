<template>
  <div class="profile__family-wrapper">
    <div class="profile__family">
      <div class="label__family">
        <label>{{ label }}</label>
        <p v-if="!isChanging">{{ value }}</p>
        <input 
          v-else 
          type="text" 
          v-model="newValue"
          @keyup.enter="saveChanges" 
          @keyup.escape="cancelChanges"
          class="family-input"
          ref="inputRef"
          :placeholder="placeholder"
        >
      </div>
      <span class="update-btn" @click="handleModify">
        {{ isChanging ? 'Enregistrer' : 'Mettre à jour' }}
      </span>
    </div>
    <div class="divider"></div>
  </div>
</template>

<script>
import { ref, nextTick } from 'vue';

export default {
  props: {
    label: String,
    value: String,
    fieldName: String, // Nouvelle prop pour identifier le champ
    placeholder:{
      type:String,
      default:'Non renseigné'
    }
  },
  emits: ['update-field'],
  setup(props, { emit }) {
    const isChanging = ref(false);
    const newValue = ref(props.value);
    const inputRef = ref(null);
    
    const saveChanges = () => {
      if (newValue.value !== props.value) {
        // Émettre l'événement avec le nom du champ et la nouvelle valeur
        emit('update-field', {
          field: props.fieldName,
          value: newValue.value
        });
      }
      isChanging.value = false;
    };
    
    const cancelChanges = () => {
      newValue.value = props.value;
      isChanging.value = false;
    };
    
    const handleModify = () => {
      if (isChanging.value) {
        saveChanges();
      } else {
        isChanging.value = true;
        nextTick(() => {
          inputRef.value?.focus();
        });
      }
    };

    return {
      isChanging,
      newValue,
      inputRef,
      handleModify,
      saveChanges,
      cancelChanges,
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
  min-width: 100px;
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
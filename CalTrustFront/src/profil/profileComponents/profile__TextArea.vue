<template>
  <div class="profile__description-wrapper">
    <div class="profile__description">
      <div class="label__description">
        <label :for="fieldId">{{ label }}</label>
        <p v-if="!isChanging">{{ value }}</p>
        <textarea
          v-else
          ref="textareaRef"
          class="description-textarea"
          rows="4"
          v-model="newValue"
          :id="fieldId"
          @keyup.enter="saveChanges"
          @keyup.escape="cancelChanges"
        ></textarea>
      </div>
      <span class="update-btn" @click="handleModify">
        {{ isChanging ? 'Enregistrer' : 'Mettre à jour' }}
      </span>
    </div>
    <div class="divider"></div>
  </div>
</template>

<script>
import { ref, computed, nextTick } from 'vue';

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
    fieldName: {
      type: String,
      default: ''
    }
  },

  emits: ['update-field'],

  setup(props, { emit }) {
    const isChanging = ref(false);
    const newValue = ref(props.value);
    const textareaRef = ref(null);

    const fieldId = computed(() =>
      props.fieldName ? `field-${props.fieldName}` : `field-${props.label.replace(/\s+/g, '-').toLowerCase()}`
    );

    const saveChanges = () => {
      if (newValue.value !== props.value) {
        emit('update-field', {
          field: props.fieldName || props.label,
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
        // La nouvelle ligne ajoutée pour le focus
        nextTick(() => {
          if (textareaRef.value) {
            textareaRef.value.focus();
          }
        });
      }
    };

    return {
      isChanging,
      newValue,
      handleModify,
      saveChanges,
      cancelChanges,
      fieldId,
      textareaRef
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
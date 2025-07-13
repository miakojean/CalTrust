<template>
  <div class="rating-container">
    <fieldset class="rating" :aria-label="ariaLabel">
      <legend v-if="showLegend" class="sr-only">{{ legendText }}</legend>
      
      <input
        v-for="i in maxRating"
        :key="`star-${i}`"
        :id="`${name}-star-${i}`"
        :name="name"
        type="radio"
        :value="i"
        :checked="modelValue === i"
        :disabled="disabled"
        @change="handleRatingChange(i)"
        class="rating-input"
      >
      <label
        v-for="i in maxRating"
        :key="`star-label-${i}`"
        :for="`${name}-star-${i}`"
        :title="`${i} ${i > 1 ? 'étoiles' : 'étoile'}`"
        class="rating-label"
      >
        <span class="sr-only">{{ i }} étoiles</span>
        <span class="star-icon">★</span>
      </label>
    </fieldset>
    
    <div v-if="showCurrentRating" class="current-rating">
      Note actuelle : {{ modelValue || 0 }}/{{ maxRating }}
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';

export default {
  name: 'StarRating',
  props: {
    modelValue: {
      type: Number,
      default: 3,
      validator: value => value >= 0
    },
    name: {
      type: String,
      default: 'rating'
    },
    maxRating: {
      type: Number,
      default: 5,
      validator: value => value > 0
    },
    disabled: {
      type: Boolean,
      default: false
    },
    showLegend: {
      type: Boolean,
      default: true
    },
    legendText: {
      type: String,
      default: 'Noter cet élément'
    },
    showCurrentRating: {
      type: Boolean,
      default: false
    },
    ariaLabel: {
      type: String,
      default: 'Système de notation'
    }
  },
  emits: ['update:modelValue'],
  setup(props, { emit }) {
    const handleRatingChange = (rating) => {
      if (!props.disabled) {
        emit('update:modelValue', rating);
      }
    };

    return {
      handleRatingChange
    };
  }
};
</script>

<style scoped>
.rating-container {
  font-family: 'Segoe UI', system-ui, sans-serif;
  display: inline-flex;
  flex-direction: column;
  gap: 0.5rem;
}

.rating {
  display: inline-flex;
  margin: 0;
  padding: 0;
  border: none;
  direction: rtl;
  unicode-bidi: bidi-override;
}

.rating-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rating-label {
  position: relative;
  cursor: pointer;
  font-size: 2rem;
  color: #e4e5e9;
  transition: color 0.2s ease, transform 0.1s ease;
}

.rating-label:hover,
.rating-label:hover ~ .rating-label,
.rating-input:checked ~ .rating-label {
  color: #1B3C53;
}

.rating-input:focus-visible + .rating-label {
  outline: 2px solid #3b82f6;
  outline-offset: 2px;
  border-radius: 2px;
}

.rating-label:active {
  transform: scale(0.9);
}

.star-icon {
  display: inline-block;
  width: 1em;
  height: 1em;
  text-align: center;
}

.current-rating {
  font-size: 0.875rem;
  color: #64748b;
  text-align: center;
}

/* Accessibilité */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

/* Thème sombre */
@media (prefers-color-scheme: dark) {
  .rating-label {
    color: #4b5563;
  }
  
  .current-rating {
    color: #9ca3af;
  }
}
</style>
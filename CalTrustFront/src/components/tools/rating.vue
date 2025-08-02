<template>
  <div class="rating-container">
    <label v-if="label" class="rating-label">{{ label }}</label>
    <div class="stars-container">
      <div class="stars__container_scd">
        <span 
        v-for="star in maxStars" 
        :key="star" 
        class="star"
        :class="[
          { 'filled': star <= internalValue, 'editable': editable },
          getRatingColorClass(internalValue)
        ]"
        @click="setRating(star)"
        @mouseover="hoverRating = editable ? star : 0"
        @mouseleave="hoverRating = 0"
        >
          {{ star <= (hoverRating || internalValue) ? '★' : '☆' }}
        </span>
      </div>

      <div class="marks">
        <input 
        type="hidden" 
        :name="name" 
        :value="internalValue"
        >
        <span v-if="showValue" class="rating-value">
          {{ internalValue }} / {{ maxStars }}
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch } from 'vue';

export default {
  name: 'Rating',
  props: {
    modelValue: {
      type: Number,
      default: 0
    },
    maxStars: {
      type: Number,
      default: 5
    },
    label: {
      type: String,
      default: 'Attribuer une note :'
    },
    name: {
      type: String,
      default: 'rating'
    },
    editable: {
      type: Boolean,
      default: true
    },
    showValue: {
      type: Boolean,
      default: true
    }
  },
  emits: ['update:modelValue'],
  setup(props, { emit }) {
    const hoverRating = ref(0);
    const internalValue = ref(props.modelValue);

    watch(() => props.modelValue, (newVal) => {
      internalValue.value = newVal;
    });

    const getRatingColorClass = (rating) => {
      if (rating === 1) return 'rating-red';
      if (rating === 2) return 'rating-orange';
      if (rating === 3) return 'rating-yellow';
      if (rating === 4) return 'rating-lightgreen';
      if (rating === 5) return 'rating-green';
      return '';
    };

    const setRating = (value) => {
      if (props.editable) {
        internalValue.value = value;
        emit('update:modelValue', value);
      }
    };

    return {
      hoverRating,
      internalValue,
      setRating,
      getRatingColorClass
    };
  }
};
</script>

<style scoped>
.rating-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 1rem;
}

.rating-label {
  font-weight: bold;
  color: #333;
}

.stars-container{
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.stars__container_scd {
  display: flex;
  gap: 0.5rem;
}

.marks{
  width: 100%;
  display: flex;
  justify-content: end;
}

.star {
  font-size: 1.8rem;
  color: #ddd;
  cursor: default;
  transition: color 0.2s;
}

.star.filled {
  color: var(--primary-color); /* Couleur des étoiles remplies */
}

.star.editable {
  cursor: pointer;
}

.star.editable:hover {
  transform: scale(1.1);
}

.rating-value {
  font-size: 0.9rem;
  color: #666;
}

/* Animation pour les étoiles */
@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.2); }
  100% { transform: scale(1); }
}

.star.editable.filled:hover {
  animation: pulse 0.5s infinite;
}

/* Animation supplémentaire pour les mauvaises notes */
.rating-red .filled {
  animation: pulse 0.5s ease infinite alternate;
}

@keyframes pulse {
  from { opacity: 0.7; }
  to { opacity: 1; }
}
</style>
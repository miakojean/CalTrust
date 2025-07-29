<template>
  <div class="decorative-rating" :aria-label="`Note : ${value} sur ${max}`">
    <span 
      v-for="i in max" 
      :key="i"
      class="star"
      :class="{
        'filled': i <= filledStars,
        'partial': showPartial && i === partialStarIndex && partialFill > 0
      }"
      :style="i === partialStarIndex ? `--fill-percentage: ${partialFill}%` : ''"
    >
      ★
    </span>
    <span v-if="showText" class="rating-text">
      {{ value.toFixed(1) }}/{{ max }}
    </span>
  </div>
</template>

<script>
export default {
  name: 'DecorativeStarRating',
  props: {
    value: {
      type: Number,
      default: 0,
      validator: v => v >= 0
    },
    max: {
      type: Number,
      default: 5
    },
    showText: {
      type: Boolean,
      default: true
    },
    size: {
      type: String,
      default: 'medium',
      validator: v => ['small', 'medium', 'large'].includes(v)
    },
    color: {
      type: String,
      default: '#f3f3f3'
    }
  },
  computed: {
    filledStars() {
      return Math.floor(this.value);
    },
    partialStarIndex() {
      return this.filledStars + 1;
    },
    partialFill() {
      return (this.value % 1) * 100;
    },
    showPartial() {
      return this.value % 1 !== 0;
    },
    sizeClass() {
      return {
        small: '1.2rem',
        medium: '1.8rem',
        large: '2.4rem'
      }[this.size];
    }
  }
};
</script>

<style scoped>
.decorative-rating {
  display: inline-flex;
  align-items: center;
  gap: 0.15rem;
  line-height: 1;
}

.star {
  font-size: v-bind('sizeClass');
  color: #e0e0e0;
  position: relative;
  display: inline-block;
  background: var(--primary-color);
}

.star.filled {
  color: v-bind('color');
}

.star.partial::before {
  content: '★';
  position: absolute;
  left: 0;
  width: var(--fill-percentage, 0%);
  overflow: hidden;
  color: v-bind('color');
}

.rating-text {
  margin-left: 0.5rem;
  font-size: 0.8rem;
  color: #666;
}
</style>
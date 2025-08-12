<template>
  <section class="global__rate">
    <div 
      v-for="(rating, index) in ratings" 
      :key="index" 
      class="stars__container"
    >
      <div class="stars">
        <span 
          class="my__star" 
          :style="{ background: rating.color }"
        >★</span>
        <p>{{ rating.stars }}</p>
      </div>
      <div 
        class="divider" 
        :style="{ width: rating.width, background: rating.color }"
      ></div>
      <p>{{ rating.count }}</p>
    </div>
  </section>
</template>

<script>
export default {
  props: {
    fiveStars: {
      type: Number,
      default: 0
    },
    fourStars: {
      type: Number,
      default: 0
    },
    threeStars: {
      type: Number,
      default: 0
    },
    twoStars: {  // ✅ Nom corrigé
      type: Number,
      default: 0
    },
    oneStar: {
      type: Number,
      default: 0
    },
  },

  setup(props) {
    const ratings = [
      { 
        stars: 5, 
        width: `${props.fiveStars}%`,  // Utilisation réelle du pourcentage
        count: props.fiveStars, 
        color: "var(--primary-color)" 
      },
      { 
        stars: 4, 
        width: `${props.fourStars}%`, 
        count: props.fourStars, 
        color: "#4CAF50" 
      },
      { 
        stars: 3, 
        width: `${props.threeStars}%`, 
        count: props.threeStars, 
        color: "#FFC107" 
      },
      { 
        stars: 2, 
        width: `${props.twoStars}%`,  // ✅ Utilise la prop corrigée
        count: props.twoStars, 
        color: "#FF9800" 
      },
      { 
        stars: 1, 
        width: `${props.oneStar}%`, 
        count: props.oneStar, 
        color: "#F44336" 
      },
    ];

    return { ratings };
  },
};
</script>

<style scoped>
.global__rate {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.stars__container {
  display: flex;
  justify-content: start;
  align-items: center;
  gap: 0.5rem;
}

.stars__container p{
  font-size: 0.9rem;
}
.stars {
  display: flex;
  font-size: 1rem;
  gap: 0.5rem;
}

.stars p{
  font-size: 0.9rem;
}
.my__star {
  padding: 0.2rem;
  color: white;
  font-size: 1rem;
  height: 1.5rem;
}

.divider {
  height: 10px;
  border-radius: 2rem;
}
</style>
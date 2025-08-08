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
  setup() {
    const ratings = [
      { stars: 5, width: "100%", count: "2K", color: "var(--primary-color)" },
      { stars: 4, width: "80%", count: "1.5K", color: "#4CAF50" },  // Vert
      { stars: 3, width: "60%", count: "1K", color: "#FFC107" },    // Jaune
      { stars: 2, width: "40%", count: "500", color: "#FF9800" },   // Orange
      { stars: 1, width: "20%", count: "200", color: "#F44336" },   // Rouge
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
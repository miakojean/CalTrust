<template>
  <div class="carousel-container">
    <button class="nav-btn prev" @click="prevSlide" aria-label="Previous">
      <i class="fas fa-chevron-left"></i>
    </button>
    
    <div class="carousel-track" ref="track">
      <div 
        v-for="(logo, index) in logos" 
        :key="index" 
        class="carousel-slide"
        :class="{ active: currentIndex === index }"
      >
        <div class="logo-container">
          <i v-if="!logo.image" :class="logo.icon || 'fas fa-building'"></i>
          <img v-else :src="logo.image" :alt="logo.name || 'Company logo'">
          <span v-if="logo.name" class="logo-name">{{ logo.name }}</span>
        </div>
      </div>
    </div>
    
    <button class="nav-btn next" @click="nextSlide" aria-label="Next">
      <i class="fas fa-chevron-right"></i>
    </button>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  props: {
    items: {
      type: Array,
      default: () => [
        { name: "TechCorp", icon: "fas fa-microchip" },
        { name: "DesignCo", icon: "fas fa-paint-brush" },
        { name: "FoodExpress", icon: "fas fa-utensils" },
        { name: "EcoWorld", icon: "fas fa-leaf" },
        { name: "FinancePlus", icon: "fas fa-chart-line" }
      ]
    },
    autoplay: {
      type: Boolean,
      default: true
    },
    interval: {
      type: Number,
      default: 3000
    }
  },

  setup(props) {
    const currentIndex = ref(0)
    const track = ref(null)
    let autoplayInterval = null

    const nextSlide = () => {
      currentIndex.value = (currentIndex.value + 1) % props.items.length
    }

    const prevSlide = () => {
      currentIndex.value = (currentIndex.value - 1 + props.items.length) % props.items.length
    }

    const startAutoplay = () => {
      if (props.autoplay) {
        autoplayInterval = setInterval(nextSlide, props.interval)
      }
    }

    onMounted(() => {
      startAutoplay()
    })

    return {
      currentIndex,
      track,
      nextSlide,
      prevSlide,
      logos: props.items
    }
  }
}
</script>

<style scoped>
.carousel-container {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  margin: 2rem auto;
  width: 100%;
  overflow: hidden;
}

.carousel-track {
  display: flex;
  transition: transform 0.5s ease;
  gap: 30px;
}

.logo-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 120px;
  height: 120px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  padding: 15px;
  transition: all 0.3s ease;
}

.logo-container:hover {
  transform: scale(1.05);
  box-shadow: 0 6px 16px rgba(0,0,0,0.15);
}

.logo-container i {
  font-size: 2.5rem;
  color: var(--primary-color);
  margin-bottom: 10px;
}

.logo-container img {
  max-width: 60px;
  max-height: 60px;
  object-fit: contain;
}

.logo-name {
  font-size: 0.9rem;
  font-weight: 600;
  text-align: center;
  color: #333;
}

.nav-btn {
  background: white;
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.nav-btn:hover {
  background: #f5f5f5;
  transform: scale(1.1);
}

.nav-btn i {
  color: #666;
}
</style>
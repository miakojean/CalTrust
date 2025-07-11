<template>
  <div class="carousel-container">
    <button class="nav-btn prev" @click="prevSlide" aria-label="Previous">
      <i class="fas fa-chevron-left"></i>
    </button>
    
    <div class="carousel-viewport">
        <div 
            class="carousel-track" 
            :style="trackStyle" 
            ref="track"
            @mouseenter="pauseAutoplay"
            @mouseleave="resumeAutoplay"
        >
        <div 
          v-for="(logo, index) in visibleLogos" 
          :key="`${index}-${logo.name}`" 
          class="carousel-slide"
          :class="{ active: centerIndex === index }"
        >
          <div class="logo-container">
            <i v-if="!logo.image" :class="logo.icon || 'fas fa-building'"></i>
            <img v-else :src="logo.image" :alt="logo.name || 'Company logo'">
            <span v-if="logo.name" class="logo-name">{{ logo.name }}</span>
          </div>
        </div>
      </div>
    </div>
    
    <button class="nav-btn next" @click="nextSlide" aria-label="Next">
      <i class="fas fa-chevron-right"></i>
    </button>
  </div>
</template>

<script>
import { ref, onMounted, computed, onUnmounted } from 'vue'

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
    },
    visibleSlides: {
      type: Number,
      default: 5
    }
  },

  setup(props) {
    const currentIndex = ref(0)
    const centerIndex = ref(Math.floor(props.visibleSlides / 2))
    const track = ref(null)
    let autoplayInterval = null

    // Duplique les éléments pour créer l'illusion d'infinite loop
    const visibleLogos = computed(() => {
      const tripleItems = [...props.items, ...props.items, ...props.items]
      const start = currentIndex.value % props.items.length
      return tripleItems.slice(start, start + props.visibleSlides)
    })

    const slideWidth = 120
    const slideGap = 30
    
    const nextSlide = () => {
      currentIndex.value = (currentIndex.value + 1) % props.items.length
    }

    const prevSlide = () => {
      currentIndex.value = (currentIndex.value - 1 + props.items.length) % props.items.length
    }
    
    const trackStyle = computed(() => {
      const centerOffset = (props.visibleSlides % 2 === 0) 
        ? (slideWidth + slideGap) / 2 
        : 0
      return {
        transform: `translateX(calc(50% - ${centerOffset}px - ${centerIndex.value * (slideWidth + slideGap)}px))`
      }
    })

    const pauseAutoplay = () => {
      if (autoplayInterval) {
        clearInterval(autoplayInterval)
      }
    }

    const resumeAutoplay = () => {
      if (props.autoplay) {
        autoplayInterval = setInterval(nextSlide, props.interval)
      }
    }

    onMounted(() => {
      if (props.autoplay) {
        autoplayInterval = setInterval(nextSlide, props.interval)
      }
    })

    onUnmounted(() => {
      pauseAutoplay()
    })

    return {
      currentIndex,
      centerIndex,
      track,
      nextSlide,
      prevSlide,
      visibleLogos,
      trackStyle,
      pauseAutoplay,
      resumeAutoplay
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
  position: relative;
}

.carousel-viewport {
  width: 100%;
  overflow: hidden;
}

.carousel-track {
  display: flex;
  gap: 30px;
  transition: transform 0.5s ease;
  will-change: transform;
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

.carousel-slide.active .logo-container {
  transform: scale(1.1);
  box-shadow: 0 6px 16px rgba(0,0,0,0.2);
  border: 2px solid var(--primary-color);
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
  background: var(--primary-color);
  color: #f5f5f5;
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
  z-index: 10;
}

.nav-btn:hover {
  background: var(--primary-color);
  transform: scale(1.1);
}

.nav-btn i {
  color: #f5f5f5;
}

@media(min-width: 766px){
  .carousel-container{
    display: flex;
    justify-content: space-around;
    align-items: center;
  }
}

/* Reste du CSS inchangé... */
</style>
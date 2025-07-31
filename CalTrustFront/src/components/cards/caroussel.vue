<template>
    <div class="carousel-container">
        <button class="nav-btn prev" @click="prevSlide" aria-label="Previous">
        <i class="fas fa-chevron-left"></i>
        </button>
        
        <div class="carousel-track" :style="trackStyle" ref="track">
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
import { ref, onMounted, computed } from 'vue' // 1. Importer 'computed'

export default {
  props: {
    items: {
      type: Array,
      default: () => [
        { name: "Restauration hotellerie", icon: "fas fa-utensils" },
        { name: "Commerce et e-commerce", icon: "fa-solid fa-dumpster"},
        { name: "Transport et logistique", icon: "ri-truck-fill" },
        { name: "Santé et bien-être", icon: "fas fa-leaf" },
        { name: "Finance Banque", icon: "fas fa-chart-line" },
        { name: "Télécommunication", icon: "fas fa-microchip" },
        { name: "Education et formation", icon: "fa-solid fa-graduation-cap"},
        { name: "Artisanat et services", icon: "fa-solid fa-bell-concierge" },
        { name: "Immobiliers", icon: "fa-solid fa-building" },
        { name: "Loisirs et divertissements", icon: "fa-solid fa-dice" },
        { name: "services publiques", icon: "fa-solid fa-building-columns" },
        { name: "Agroindustrie", icon: "fa-solid fa-wheat-awn" }
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

    // 2. Définir les dimensions pour le calcul du décalage
    const slideWidth = 120 // La largeur de .logo-container
    const slideGap = 30   // Le gap dans .carousel-track
    
    const nextSlide = () => {
      currentIndex.value = (currentIndex.value + 1) % props.items.length
    }

    const prevSlide = () => {
      currentIndex.value = (currentIndex.value - 1 + props.items.length) % props.items.length
    }
    
    // 3. Créer une propriété calculée pour le style du 'track'
    const trackStyle = computed(() => {
      // Calcule le décalage total : index * (largeur + espacement)
      const offset = currentIndex.value * (slideWidth + slideGap)
      return {
        transform: `translateX(-${offset}px)`
      }
    })

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
      logos: props.items,
      trackStyle // 4. Exposer la propriété calculée au template
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
  width: 65%;
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
  cursor: pointer;
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
</style>
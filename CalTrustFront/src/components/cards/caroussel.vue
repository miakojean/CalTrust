<template>
    <div class="carousel-container"
      @mouseenter="pauseAutoplay" 
      @mouseleave="startAutoplay"
    >
      <button class="nav-btn prev" @click="prevSlide" aria-label="Previous">
      <i class="fas fa-chevron-left"></i>
      </button>
      
      <div class="carousel-track" :style="trackStyle" ref="track">
        <div 
          v-for="(logo, index) in logos" 
          :key="index" 
          class="carousel-slide"
          :class="{ active: currentIndex === index }"
          @click="() => makeQuery(logo)"
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
import { ref, onMounted, onUnmounted, computed } from 'vue'
import api from '@/_services/_authservices'

export default {
  props: {
    items: {
      type: Array,
      default: () => [
        { name: "Restauration hotellerie", icon: "fas fa-utensils", code :"RH" },
        { name: "Commerce et e-commerce", icon: "fa-solid fa-dumpster", code :"CE"},
        { name: "Transport et logistique", icon: "ri-truck-fill", code :"TL" },
        { name: "Santé et bien-être", icon: "fas fa-leaf", code :"SB" },
        { name: "Finance Banque", icon: "fas fa-chart-line", code :"FB" },
        { name: "Télécommunication", icon: "fas fa-microchip", code :"TC" },
        { name: "Education et formation", icon: "fa-solid fa-graduation-cap", code :"EF"},
        { name: "Artisanat et services", icon: "fa-solid fa-bell-concierge", code :"AS" },
        { name: "Immobiliers", icon: "fa-solid fa-building", code :"IM" },
        { name: "Loisirs et divertissements", icon: "fa-solid fa-dice", code :"LD" },
        { name: "services publiques", icon: "fa-solid fa-building-columns", code :"SP" },
        { name: "Agroindustrie", icon: "fa-solid fa-wheat-awn", code :"AI" }
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

    const pauseAutoplay = () => {
      if (autoplayInterval) {
        clearInterval(autoplayInterval)
        autoplayInterval = null
      }
    }

    onMounted(() => {
      startAutoplay()
    })

    // N'oubliez pas de nettoyer l'intervalle lorsque le composant est démonté
    onUnmounted(() => {
      pauseAutoplay()
    })

    const makeQuery = async (logo) => {
      console.log('Logo cliqué:', logo)
      
      if (!logo.code) {
        console.error('Aucun code de catégorie trouvé pour ce logo')
        return
      }

      console.log(`Préparation de la requête pour la catégorie: ${logo.code}`)
      
      try {
        console.log(`Envoi de la requête GET à /companies/search/?category=${logo.code}`)
        
        const response = await api.get(`/companies/search/?category=${logo.code}`, {
          headers: { 'Accept': 'application/json' }
        })

        console.log('Réponse reçue:', response)
        
        if (!response.data) {
          console.error('Réponse vide de l\'API')
          throw new Error('Réponse vide de l\'API')
        }

        console.log('Données reçues:', response.data)
        return response.data
      } catch (error) {
        console.error("Erreur lors de la récupération des entreprises:", error)
        throw new Error(`Impossible de charger les entreprises: ${error.message}`)
      }
    }

    return {
      currentIndex,
      track,
      nextSlide,
      prevSlide,
      logos: props.items,
      trackStyle, // 4. Exposer la propriété calculée au template
      startAutoplay,
      pauseAutoplay,
      makeQuery
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
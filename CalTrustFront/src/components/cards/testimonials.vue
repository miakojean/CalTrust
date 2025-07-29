<template>
  <article class="testimonial-card">
    <div class="message">
        <p class="message__body">
            {{ message }}
        </p>
    </div>
    <fake-rating 
        :value="rating" 
        :max="5"
        color="#1B3C53"
        size="small"
    />
    <div class="divider"></div>
    <div class="profile">
        <img class="pp" :src="pic" alt="fake profile picture">
        <div class="profile__info">
            <span>{{ info }}</span>
            <p class="message__body">@{{username}}</p>
        </div>
    </div>

  </article>
</template>

<script>
import fakeRating from '../tools/fakeRating.vue';
import { computed } from 'vue';

const defaultPic = new URL('@/assets/Pictures/fakepropfilepic.jpg', import.meta.url).href;

export default {
    props:{
        message:{
            type: String,
            default:"Bienvenu au pays mon fils"
        },
        info:{
            type: String,
            default:"John Doe"
        },
        username:{
            type: String,
            default: 'unknown'
        },
        pic:{
            type: String,
            default: defaultPic
        },
        rating: { 
            type: Number,
            default: 4,  // Valeur par défaut
            validator: (value) => {
                return value >= 0 && value <= 5;  // Validation entre 0 et 5
            }
        }
    },

    components:{
        fakeRating
    },

    setup(props) {
        const defaultPic = new URL('@/assets/Pictures/fakepropfilepic.jpg', import.meta.url).href;
        const profilePic = computed(() => props.pic || defaultPic);

        return { profilePic };
    }

}
</script>

<style scoped>
.testimonial-card {
  display: flex;
  flex-direction: column;
  align-items: normal;
  gap: 0.5rem;
  padding: 1.5rem;
  border-radius: 1rem;
  background: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 400px;

}

.divider {
  height: 2px;
  background: var(--primary-color); /* Couleur grise légère */
  margin: 24px 0; /* Espacement vertical */
}

.profile{
    width: 100%;
    display: flex;
    justify-content: start;
    align-items: center;
    gap: 2rem;
}

.pp{
    height: 60px;
    width: 60px;
    border-radius: 50%;
}

.profile__info{
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    align-items: center;
}

.profile__info span{
    font-weight: 500;
    font-size: 1rem;
    color: var(--primary-color);
}

@media (min-width: 766px) {
    .message__body{
        font-size: 0.8rem;
        text-align: start;
    }
}

@media (min-width: 1260px) {
    .message__body{
        font-size: 0.8rem;
        text-align: start;
    }
}
</style>
<template>
  <article class="testimonial-card">
    <div class="profile">
        <div class="pp__firm">
            <span>CA</span>
        </div>
        <div class="profile__info">
            <span>{{ company }}</span>
        </div>
    </div>

    <ratingTools 
        :rating="rating" 
        :max="5"
        size="small"
    />
    
    <div class="divider"></div>

    <div class="message">
        <p class="message__body">
            {{ message }}
        </p>
    </div>
    
    <div class="profile">
        <img class="pp" :src="pic" alt="fake profile picture">
        <div class="profile__info">
            <span>{{ info }}</span>
            <p class="message__body">@{{username}}</p>
        </div>
    </div>
    
    <div class="divider__two"></div>

    <div class="utility">
        <p class="is_right">Trouvez-vous cet avis utile?</p>
        <i @click="iLikeIt()" 
            class="ri-thumb-up-line"
            v-if="isUseful === false"
        ></i>

        <i class="ri-thumb-up-fill"
            @click="iLikeIt()"
            v-else 
        ></i>

    </div>

  </article>
</template>

<script>
import { computed, ref } from 'vue';
import ratingTools from '../rating/ratingTools.vue';

const defaultPic = new URL('@/assets/Pictures/fakepropfilepic.jpg', import.meta.url).href;

export default {
    props:{

        company:{
            type:String,
            default:'anonymous'
        },
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
        ratingTools
    },

    setup(props) {
        const defaultPic = new URL('@/assets/Pictures/fakepropfilepic.jpg', import.meta.url).href;
        const profilePic = computed(() => props.pic || defaultPic);

        const isUseful = ref(false)

        function iLikeIt () {
            if (isUseful.value === false){
                isUseful.value = true
            } else if (isUseful.value === true){
                isUseful.value = false
            }
        }

        return { profilePic, isUseful, iLikeIt };
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
  cursor: pointer;

}

.divider {
  height: 2px;
  background: var(--primary-color); /* Couleur grise légère */
  margin: 12px 0; /* Espacement vertical */
}

.divider__two {
  height: 1px;
  background: #d8d8d8; /* Couleur grise légère */
  margin: 0.5rem 0; /* Espacement vertical */
}

.profile{
    width: 100%;
    display: flex;
    justify-content: start;
    align-items: center;
    gap: 1rem;
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
    justify-content: start;
}

.profile__info span{
    font-weight: 500;
    font-size: 1rem;
    color: var(--primary-color);
}

.pp__firm{
    height: 50px;
    width: 50px;
    border-radius: 50%;
    background: #d87422;
    display: flex;
    justify-content: center;
    align-items: center;
}

.pp__firm span{
    color: white;
    font-weight: 600;
}

.utility{
    display: flex;
    justify-content: start;
    gap: 0.5em;
}

.utility i {
    cursor: pointer;

}

.utility i:hover {
    cursor: pointer;
    
}

.is_right{
    font-size: 0.8rem;
    width: 100%;
    text-align: start;
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
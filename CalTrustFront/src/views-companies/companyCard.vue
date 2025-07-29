<template>
    <article class="testimonial-card">
        <div class="profile">
            <div class="pp">
                <span>CA</span>
            </div>
            <div class="profile__info">
                <span>{{ firm }}</span>
                <p class="message__body">{{ category }}</p>
            </div>
        </div>
        <div class="divider"></div>
        <rating-component/>
        <div class="btn__frame">
            <cardMainButton/>
            <cardMoreButton/>
        </div>
    </article>
</template>

<script>
import fakeRating from '@/components/tools/fakeRating.vue';
import cardMainButton from '@/components/button/cardMainButton.vue';
import cardMoreButton from '@/components/button/cardMoreButton.vue';
import ratingComponent from '@/components/tools/ratingComponent.vue';
import { computed } from 'vue';
import RatingComponent from '../../../CalTrustFront/src/components/tools/ratingComponent.vue';

const defaultPic = new URL('@/assets/pictures/devnomicus.png', import.meta.url).href;

export default {
    props:{
        firm:{
            type: String,
            default:"Caladrius"
        },
        category:{
            type: String,
            default: 'fintech'
        },
        pic:{
            type: String,
            default: defaultPic
        }
    },

    components:{
        fakeRating, cardMainButton, cardMoreButton, ratingComponent,
        RatingComponent
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
  gap: 1rem;
  padding: 0.5rem;
  border-radius: 1rem;
  background: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 400px;
}

.divider {
  height: 2px;
  background: var(--primary-color); /* Couleur grise légère */
  margin: 1rem 0; /* Espacement vertical */
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
    background: #d87422;
    display: flex;
    justify-content: center;
    align-items: center;
}

.pp span{
    color: white;
    font-weight: 600;
}

.profile__info{
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    align-items: center;
}

.profile__info span{
    font-weight: 600;
    font-size: 1rem;
    color: var(--primary-color);
}

.btn__frame{
    width: 100%;
    display: flex;
    justify-content: start;
    align-items: center;
    gap: 0.5rem;
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
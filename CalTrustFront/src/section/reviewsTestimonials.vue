<template>
  <section class="reviews__section">
    <second-stepper title="Consulter les avis récents"/>
    <div class="testimonial__container">
        <testimonials/>
        <testimonials
        info="Jane Doe"/>
        <testimonials/>
        <testimonials
        info="Jane Doe"/>
    </div>
  </section>
</template>

<script>
import SecondStepper from '@/components/cards/secondStepper.vue';
import testimonials from '@/components/cards/testimonials.vue';
export default {
    components:{
        testimonials,
        SecondStepper
    },

    setup(){
        const jane = new URL('@/assets/Pictures/fakepropfilepic.jpg', import.meta.url).href;

        return{
            jane
        }
    }
}
</script>

<style scoped>
.reviews__section{
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1rem;
}

.testimonial__container{
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

@media(min-width:766px) {
    .testimonial__container{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
    }
}

@media(min-width: 1260px) {
    .testimonial__container{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 1rem;
    }
}
</style>
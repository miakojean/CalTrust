<template>
  <section class="main__section">
    <div class="main__container">
        <h2>
            We have worked with thousands of amazing people
        </h2>
    </div>
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
import testimonials from '@/components/cards/testimonials.vue';
export default {
    components:{
        testimonials,
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
.testimonial__container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1rem;
}

@media(min-width:766px) {
    .testimonial__container{
        display: grid;
        grid-template-columns: 1fr 1fr;
    }
}
</style>
<template>
    <section class="main__section">
        <div class="main__container">
            <h1>
                We're changing the way people connect
            </h1>
            <p>
                Lorem ipsum dolor sit amet consectetur 
                adipisicing elit. Pariatur impedit eaque 
                ipsa culpa recusandae temporibus, non 
                cumque nostrum laborum quibusdam?
            </p>
            <div class="btn__flex">
                <main-button></main-button>
                <more-button/>
            </div>
        </div>
        <div class="pic__container">
            
        </div>
    </section>
</template>

<script>
import mainButton from '@/components/button/mainButton.vue';
import moreButton from '@/components/button/moreButton.vue';
export default {
    components:{
        mainButton, moreButton
    }
}
</script>

<style>

</style>
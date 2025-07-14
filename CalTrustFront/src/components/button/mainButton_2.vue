<template>
  <button class="main__button">
    <loader/>
  </button>
</template>

<script>
import loader from '../tools/loader.vue';
export default {

    props:{
        label:{
            type: String,
            default: 'Get Started'
        }
    },
    components:{
        loader
    }

}
</script>

<style scoped>
.main__button{
    background: var(--tertiary-color);
    color: var(--primary-color);
    transition: 0.5s;
    border-radius: 0.4rem;
    width: 50%;
    max-width: 200px;
    font-weight: 600;
    transition: ease-in-out 0.3s;
    display: flex;
    justify-content: center;
    align-items: center;
}

.main__button:hover{
    background: #f5bb94;;
    transition: ease-in-out 0.3s;
}
</style>
<template>
  <button class="second__button">
    {{ label }}
  </button>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
    props:{
        label:{
            type:String,
            default: "inscription"
        }
    },
    setup () {
        
    }
}

</script>

<style scoped>
.second__button{
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.8rem;
    font-size: 0.9rem;
    width: 50%;
    max-width: 100px;
    transition: 0.7s ease-in-out;
}

.second__button:hover {
    transition: 0.5s ease-in-out;
}
</style>
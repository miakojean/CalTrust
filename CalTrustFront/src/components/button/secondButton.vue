<template>
  <button @click="registration" class="second__button">{{ label }}
    <i class="ri-contract-right-line"></i>
  </button>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
    props:{
        label:{
            type:String,
            default: "Inscription"
        }
    },
    setup () {
        const router = useRouter();
        const registration = () => {
            router.push('/registration');
        };
        return {registration};
    }
}

</script>

<style scoped>
.second__button{
    display: flex;
    gap: 0.5rem;
    padding: 0.8rem;
    font-size: 0.9rem;
    width: 100%;
    transition: 0.7s ease-in-out;
}

.second__button:hover {
    transition: 0.5s ease-in-out;
}
</style>
<template>
  <div class="box__connexion">
    <h2>Rejoignez notre communauté dès maintenant !</h2>
    <mainButton @click="registration" label="j'ouvre mon compte" width="40%"/>
  </div>
</template>

<script>
import mainButton from '@/components/button/mainButton.vue';
import { useRouter } from 'vue-router';
export default {
    components:{
        mainButton
    },
    setup() {
        const router = useRouter();
        const registration = () => {
            router.push('/registration'); // Redirection vers la page d'inscription
        };
        return { registration };
    }
}
</script>

<style>
.box__connexion{
    border: none;
    padding: 1rem;
    background: linear-gradient(179deg,rgba(27, 60, 83, 1) 0%, rgba(186, 186, 186, 1) 89%, rgba(252, 252, 250, 1) 100%);
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    border-radius: 1rem;
    gap: 1rem;
    width: 100%;
}
.box__connexion h2{
    color: #fff;
}

@media(min-width:766px) {
    .box__connexion{
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;
        height: 40vh;
    }
}
</style>
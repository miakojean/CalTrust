<template>
  <div class="box__connexion">
    <h2>Ouvrez votre compte dès maintenant</h2>
    <mainButton label="j'ouvre mon compte"/>
  </div>
</template>

<script>
import mainButton from '@/components/button/mainButton.vue';
export default {
    components:{
        mainButton
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
<template>
  <section class="login__section">
    <div class="main__container">
      <p>Bienvenu chez nous</p>
      <h2 class="text__illus">
        Inscription
      </h2>
      <regisForm/>
    </div>
    <div class="illustrations__container">
      <img class="svg" src="../assets/svg/undraw_reviews_ukai.svg" alt="">
    </div>
  </section>
</template>

<script>
import regisForm from './regisForm.vue';
import stepper from '@/components/cards/stepper.vue';
export default {
  components:{
    regisForm, stepper
  }
}
</script>

<style scoped>
.login__section{
  width: 100%;
  min-height: 100vh;
}

.main__container{
  padding-top: 1rem;
  gap: 1rem;
  width: 100%;
}

.text__illus{
    width: 100%;
    text-align: start;
}

.illustrations__container{
  display: none;
}

@media (min-width: 1024px) {

  .login__section{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    gap: 2rem;
  }

  .illustrations__container{
    display: flex;
  }

  .svg{
    width: 100%;
    height: 100%;
  }

  .main__container{
    padding-top: 1rem;
    gap: 1rem;
    width: 70%;
  }

  .text__illus{
    width: 70%;
    text-align: start;
  }

  .login__label {
    font-size: 0.8rem;
    text-align: center;
    width: 100%;
  }
}
</style>
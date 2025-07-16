<template>
  <section class="login__section">
    <div class="main__container">
      <h2 class="text__illus">
        Connexion
      </h2>
      <p class="text__illus">
        Nous ferons pleine de belles choses ensemble
      </p>
      <ourForm/>
    </div>
    <div class="illustrations__container">
      <img class="svg" src="../assets/svg/undraw_reviews_ukai.svg" alt="">
    </div>
  </section>
</template>

<script>
import ourForm from '@/components/tools/ourSigninForm.vue';
import stepper from '@/components/cards/stepper.vue';
export default {
  components:{
    ourForm, stepper
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
  gap: 0.5rem;
  width: 100%;
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
    text-align: center;
  }

  .login__label {
    font-size: 0.8rem;
    text-align: center;
    width: 100%;
  }
}
</style>
<template>
  <section class="login__section">
    <div class="main__container">
      <ourForm/>
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
}

.main__container{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
  width: 100%;
}

.login__label{
  text-align: center;
  width: 100%;
}

@media (min-width: 1024px) {

  .main__container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 0.5rem;
    width: 100%;
  }

  .login__label {
    font-size: 0.8rem;
    text-align: center;
    width: 100%;
  }
}
</style>
<template>
  <section class="login__section">
    <div class="main__container">
      <p>Se connecter</p>
      <ourForm/>
    </div>
    <div class="pic__container">
      <img class="pair" src="@/assets/Pictures/picture_seven.jpg" alt="Reunion of people" />
      <img class="impair" src="@/assets/Pictures/picture_six.jpg" alt="Reunion of people" />
      <img class="pair" src="@/assets/Pictures/picture_one.jpg" alt="Reunion of people" />
      <img class="impair" src="@/assets/Pictures/picture_four.jpg" alt="Reunion of people" /> 
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

<style>
.login__section{
  min-height: 100vh;
}

.pic__container{
  display: none;
}
</style>
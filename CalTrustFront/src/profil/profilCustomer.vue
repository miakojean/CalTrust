<template>
    <div class="profil">
      <sencond-stepper title="Mon profil"/>
        <h2>Bienvenue dans votre profil</h2>
      <Transition>
        <p v-if="message.error" style="color: red;">{{ message.error }}</p>
      </Transition>
      <Transition>
        <p v-if="message.success" style="color: green;">{{ message.success }}</p>
      </Transition>
    </div>
    
  </template>
  
  <script>
  export default {
  
  }
  </script>
  
  <style>
  
  </style>
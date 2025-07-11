<template>
  <div class="input__family flex__center">
    <label for="">{{ label }}</label>
    <input :type=type  :placeholder="placeholder">
  </div>
</template>

<script>
export default {

    props:{
        label:{
            type:String,
            default:"username"
        },
        type:{
            type:String,
            default:"text"
        },
        placeholder:{
            type: String,
            default: "Entrer votre nom d'utilisateur" // <- Correction ici
        }
    }

}
</script>

<style scoped>
label{
    color: var(--near-white);
}

input{
    background: none;
    border: 1px solid var(--near-white);
    color: var(--near-white);
    font-weight: 500;
}

</style>
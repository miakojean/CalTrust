<template>
  <div class="input__family flex__center">
    <label for="">{{ label }}</label>
    <input 
        :type=type  
        :placeholder="placeholder"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
    >
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
        },
        modelValue: {
            type: String,
            default: ""
        }
        
    },
    emits: ['update:modelValue']

}
</script>

<style scoped>
label{
    color: var(--primary-color);
}

input{
    background: none;
    border: 1px solid var(--primary-color);
    color: var(--primary-color);
    font-weight: 500;
}

@media (min-width: 1024px) {
    label{
        font-size: 0.8rem;
        width: 100%;
    }
}

</style>
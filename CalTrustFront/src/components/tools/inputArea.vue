<template>
  <div class="input__family flex__center">
    <label for=""><h4>{{ label }}</h4></label>
    <textarea
        :type=type  
        :placeholder="placeholder"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
    >
    </textarea>
  </div>
</template>

<script>
export default {

    props:{
        label:{
            type:String,
            default:"Votre expérience"
        },
        type:{
            type:String,
            default:"text"
        },
        placeholder:{
            type: String,
            default: "Comment s'est passé votre expérience" // <- Correction ici
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
.input__family{
    width:100%;
}

label{
    color: var(--primary-color);
    font-size: 0.8rem;
}

label h4{
    font-size: 1rem;
}

input{
    background: none;
    color: var(--primary-color);
    font-weight: 500;
    font-size: 0.8rem;
    background: #eeeeee;
    transition: ease-in-out 0.8s;
}

input:focus{
    background: #d6e4ee;
    transition: ease-in-out 0.5s;
}

input:hover{
    background: #d6e4ee;
    transition: ease-in-out 0.5s;
    cursor: text;
}

@media (min-width: 1024px) {
    label{
        font-size: 0.8rem;
        width: 100%;
    }

    .input__family{
        width: 100%;
    }
}

</style>
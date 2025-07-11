<template>
  <button class="main__button">
    {{ label }}
  </button>
</template>

<script>
export default {

    props:{
        label:{
            type: String,
            default: 'Get Started'
        }
    }

}
</script>

<style scoped>
.main__button{
    background: var(--tertiary-color);
    color: var(--primary-color);
    transition: 0.5s;
    border-radius: 0.4rem;
    width: 50%;
    max-width: 200px;
    font-weight: 600;
    transition: ease-in-out 0.3s;
}

.main__button:hover{
    background: #f5bb94;;
    transition: ease-in-out 0.3s;
}
</style>
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
    background: var(--primary-color);
    color: #fff;
    transition: 0.5s;
    border-radius: 0.4rem;
    width: 70%;
    max-width: 200px;
}

.main__button:hover{
    background: #1e5179;
    transition: ease-in-out 0.3s;
}
</style>
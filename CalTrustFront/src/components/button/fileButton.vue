<template>
  <button class="more__button" :style="{ width: width }">
    {{ label }}
    <i class="ri-upload-2-line"></i>
  </button>
</template>

<script>
export default {

    props:{
        label:{
            type: String,
            default: 'Get More'
        },
        width: {
            type: String,
            default: 'auto'
        }
    }

}
</script>

<style scoped>
.more__button{
    background: #f3f3f3;
    color: #111;
    transition: 0.5s;
    width: 100%;
    max-width: 300px;
}

.more__button:hover{
    background: #d6d6d6;
    transition: ease-in-out 0.3s;
}
</style>
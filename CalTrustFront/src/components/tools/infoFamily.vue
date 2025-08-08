<template>
  <div class="info__family">
    <span><i :class="icon"></i> {{ label }}:</span>
    <p>{{ info }}</p>
  </div>
</template>

<script>
export default {

    props:{
        icon:{
            type:String,
            default:'ri-phone-line'
        },
        label:{
            type:String,
            default: "Phone"
        },
        info:{
            type:String,
            default:'0102030405'
        }
    }

}
</script>

<style scoped>
    .info__family{
        padding: 0.5rem 0;
        display: flex;
        align-items: center;
        justify-content: start;
        gap: 1rem;
    }

    .info__family span{
        display: flex;
        align-items: center;
        justify-items: start;
        font-weight: 500;
        gap: 0.5rem;
        color: #8d8d8d;
        font-size: 0.9rem;

    }

    .info__family span i{
        background: #d8d8d8;
        color: var(--primary-color);
        font-size: 0.9rem;

    }

    .info__family p{
        color: var(--primary-color);
        font-weight: 600;
        font-size: 0.9rem;
    }
</style>
<template>
  <div class="footer__card flex__center">
    <h4 class="title">{{ title }} </h4>
    <ul>
      <li v-for="item in tables" :key="item">
        {{ item }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: "Solutions"
    },
    tables: {
      type: Array,
      default: () => ['Marketing', 'Analytique', 'Automation', 'Commerce', 'Insights']
    }
  }
}
</script>

<style scoped>

.title{
    padding-bottom: 1rem;
    font-size: 1.2rem;
    font-weight: 600;
}

li{
    padding-bottom: 1rem;
    font-size: 0.8rem;
}
</style>
<template>
  <div class="loader">
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
  </div>
</template>

<style scoped>
  .loader {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: none;
  }

  .bar {
    display: inline-block;
    width: 3px;
    height: 1.2rem;
    background-color: var(--primary-color);
    border-radius: 10px;
    animation: scale-up4 1s linear infinite;
  }

  .bar:nth-child(2) {
    height: 0.9rem;
    margin: 0 5px;
    animation-delay: .25s;
  }

  .bar:nth-child(3) {
    animation-delay: .5s;
  }

  @keyframes scale-up4 {
    20% {
      background-color: var(--primary-color);
      transform: scaleY(1.5);
    }

    40% {
      transform: scaleY(1);
    }
  }
</style>

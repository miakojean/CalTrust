<template>
  <div class="card">
    <div class="card__head">
      <div class="pp skeleton"></div>
      <div class="pp__info">
        <span class="skeleton"></span>
        <span class="skeleton"></span>
      </div>
    </div>
    
    <div class="card___body skeleton"></div>
    
    <div class="btn">
      <span class="span_btn skeleton"></span>
      <span class="span_btn skeleton"></span>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
/*
  The new skeleton animation styles
*/
@keyframes pulse {
  0% {
    background-position: -200px 0;
  }
  100% {
    background-position: 200px 0;
  }
}

.skeleton {
  background: linear-gradient(90deg, #e8e8e8 25%, #f5f5f5 50%, #e8e8e8 75%);
  background-size: 200px 100%;
  animation: pulse 1.5s infinite ease-in-out;
}

/*
  Your existing styles, with background colors removed and replaced by the .skeleton class
*/
.card {
  max-width: 350px;
  width: 100%;
  background: #ffffff;
  padding: 20px;
  border-radius: 8px;
  border: 1px solid #eaeaea;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.card__head{
  display: flex;
  justify-content: start;
  align-items: center;
  gap: 1rem;
  background: none;
  height: 80px;
}

.pp{
  /* background: #d8d8d8; -- REMOVED */
  height: 60px;
  width: 60px;
  border-radius: 50%;
}

.pp__info{
  height: 60px;
  width: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.pp__info span {
  height: 8px;
  /* background: #d8d8d8; -- REMOVED */
  width: 100%;
  display: block;
}

.card___body{
  /* background: #f3f3f3; -- REMOVED */
  border-radius: 16px;
  height: 150px;
}

.btn{
  display: flex;
  gap: 1rem;
}

.span_btn {
  height: 16px;
  padding: 1rem;
  border-radius: 1rem;
  /* background: #d8d8d8; -- REMOVED */
  width: 100%;
  display: block;
}
</style>
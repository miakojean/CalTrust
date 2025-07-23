<template>
  <div class="section-divider">
    <div class="divider-title">
      <span class="text">{{ title }}</span>
      <span class="line"></span>
    </div>
    <div class="content">
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
// Ce composant accepte une propriété "title" pour afficher le texte du séparateur
defineProps({
  title: {
    type: String,
    default: 'Inscription client'
  }
});
</script>

<style scoped>
.section-divider {
  width: 100%;
}

.divider-title {
  display: flex;
  align-items: center;
  text-align: start;
  color: var(--primary-color); /* Couleur du texte discrète */
}

/* Les lignes de chaque côté du texte */
.line {
  flex-grow: 1; /* Permet aux lignes de prendre toute la place disponible */
  height: 1px;
  background-color: rgb(218, 218, 218); /* Couleur de la ligne */
}

/* Le texte au milieu */
.text {
  padding: 0 1rem; /* Espace entre le texte et les lignes */
  font-size: 1.1rem;
  font-weight: 600;
  letter-spacing: 0.5px;
}

/* Le conteneur pour votre contenu */
.content {
  margin-top: 0.5rem; /* Espace entre le séparateur et le contenu en-dessous */
}


</style>
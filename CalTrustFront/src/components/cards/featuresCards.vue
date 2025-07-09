<template>
    <div class="features__cards">
        <span>
            <i :class="icon"></i> <!-- Utilisation directe de la prop -->
        </span>
        <h3 class="features__title">{{ title }}</h3>
        <p class="features__subtitle">
            {{ subtitle }}
        </p>
    </div>
</template>

<script>
export default {
    props: {
        title: {
            type: String,
            default: 'Avis Vérifiés'
        },
        subtitle: {
            type: String,
            default: "Seuls les avis provenant de clients authentiques sont publiés..."
        },
        icon: {
            type: String,
            default: "fas fa-check-circle" // Valeur par défaut ici plutôt que dans setup()
        }
    }
    // Pas besoin de setup() si vous n'avez pas de logique supplémentaire
}
</script>

<style scoped>
.features__title, .features__subtitle{
  color: #fff;
}

</style>
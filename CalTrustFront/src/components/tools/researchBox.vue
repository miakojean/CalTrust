<template>
    <div class="research__box">
        <label for="firms">Je cherche des avis sur</label>
        <div class="input__family">
            <input type="text" id="firms" placeholder="Trouver un service, une entreprise, un produits">
            <button class="research__button">
                <i class="fas fa-search"></i>
            </button>
        </div>
        
    </div>
</template>

<script>

export default {
    components:{
        
    }
}
</script>

<style>
.research__box{
    width: 100%;
    gap: 1rem;
    display: flex;
    flex-direction: column;
    justify-content: start;
    border-radius: 1rem;
}

.input__family{
    width: 100%;
    display: flex;
    gap: 1rem;
}



.research__button{
    padding: 1rem;
    border-radius: 50%;
    height: 100%;
    background: #358cd3;
    color: #fff;
    font-size: 1.1rem;
    transition: ease-in-out 1.2s;
}

.research__button:hover{
    background: #114977;
    color: #fff;
    transition: ease-in-out 0.8s;
}

</style>
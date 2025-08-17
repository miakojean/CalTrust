<template>
  <div class="profile__container">
    <h4>Profile</h4>
    <p>This information will be displayed publicly so be careful what you share.</p>
    <stepper/>
    <Profile__family
        v-for="(i, index) in profile"
        :key="index"
        :label="i.label"
        :value="i.value"
    />
  </div>
</template>

<script>
import stepper from '@/components/cards/stepper.vue';
import Profile__family from './profile__family.vue';
export default {

    components:{
        stepper,
        Profile__family
    },

    setup(){
        const profile = [
            {label:'Nom de famille', value:"MIAKO"},
            {label:'Prenom', value:"Jean Yves Arnold"},
            {label:'Email', value:"miakojeanyves@gmail.com"},
        ]

        return{profile}
    }

}
</script>

<style scoped>
.profile__container{
    display: flex;
    flex-direction: column;
    justify-content: start;
    gap: 0.5rem;
    width: 100%;
}

.profile__container h4,p{
    text-align: start;
}

h4{
    font-size: 1.1rem;
}

p{
    font-size: 0.9rem;
    font-weight: 400;
}
</style>
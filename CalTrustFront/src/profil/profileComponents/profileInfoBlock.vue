<template>
  <div class="main__container">
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
            {label:'Nom de famille', value:"MIAKO"},
            {label:'Nom de famille', value:"MIAKO"},
        ]

        return{profile}
    }

}
</script>

<style>

</style>
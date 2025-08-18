<template>
  <div class="profile__container">
    <h4>{{ title }}</h4>
    <p>{{ description }}</p>

    <div class="divider"></div>

    <profile__fileUpload
        v-if="uploadFile === true"
        accept="image/*,.pdf"
        :maxSize="5 * 1024 * 1024" 
    />
    
    <Profile__family
        v-for="(i, index) in fields"
        :key="index"
        :label="i.label"
        :value="i.value"
    />

    <profile__TextArea
        v-if="isThereDescription === true"
    />

    <profile__Toggle
        v-if="isThereToggle === true"
    />
  </div>
</template>

<script>
import stepper from '@/components/cards/stepper.vue';
import Profile__family from './profile__family.vue';
import profile__TextArea from './profile__TextArea.vue';
import profile__Toggle from './profile__Toggle.vue';
import uploadFile from '@/components/tools/file/uploadFile.vue';
import profile__fileUpload from './profile__fileUpload.vue';
export default {

    components:{
        stepper,
        Profile__family,
        profile__TextArea,
        profile__Toggle,
        uploadFile,
        profile__fileUpload
    },

    props:{
        title:{
            type:String,
            default:'Informations de base'
        },
        description:{
            type:String,
            default:'Cette section présente les différentes information de base de votre entreprise '
        },
        fields: {
            type: Array,
            default: () => [
                { label: 'Nom de l\'entreprise', value: "Caladrius" },
                { label: 'Adresse', value: "303 Firewall Lane, Safe Harbor" },
                { label: 'Email', value: "firm6@business.com" },
                {label:'Téléphone', value:"0102030405"}
            ]
        },
        isThereDescription:{
            type:Boolean,
            default:true
        },
        isThereToggle:{
            type:Boolean,
            default:true
        },
        uploadFile:{
            type:Boolean,
            default: true
        }
    },

    setup(){
        

        return{}
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
    font-size: 1rem;
}

p{
    font-size: 0.9rem;
    font-weight: 400;
}

.divider {
  height: 2px;
  background: #d8d8d8; /* Couleur grise légère */
  margin: 1rem 0; /* Espacement vertical */
}
</style>
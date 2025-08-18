<template>
    <div class="input__family">
      <label :for="label">{{ label }}</label>
      <select 
        :id="label"
        v-model="inputValue"
        @change="updateValue"
      >
      <option></option>
      <option 
        v-for="(item, index) in options" 
        :key="index" 
        :value="getOptionValue(item)"
      >
        {{ getOptionLabel(item) }}
      </option>
      </select>
    </div>
</template>
  
<script>
  import { ref, watch } from 'vue';
  
  export default {
    props: {
      label: {
        type: String,
        default: "Tranche d'âge"
      },
      options: {
        type: Array,
        default: () => ['0-18', '19-25', '26-35', '36-45', '46-55', '56+']
      },
      modelValue: {
        type: [String, Number, Object],
        default: ''
      }
    },
    emits: ['update:modelValue'],
    setup(props, { emit }) {
      const inputValue = ref(props.modelValue);

      // Fonction pour gérer à la fois les options simples (string) et complexes (objets)
      const getOptionLabel = (option) => {
        return typeof option === 'object' ? option.label : option;
      };

      // Fonction pour obtenir la valeur de l'option
      const getOptionValue = (option) => {
        return typeof option === 'object' ? option.value : option;
      };

      // Met à jour la valeur parente quand inputValue change
      const updateValue = () => {
        emit('update:modelValue', inputValue.value);
      };

      // Synchronise inputValue si modelValue change depuis le parent
      watch(() => props.modelValue, (newVal) => {
        inputValue.value = newVal;
      });

      return {
        inputValue,
        updateValue,
        getOptionLabel,
        getOptionValue
      };
    }
  }
</script>
  
<style scoped>
  .input__family{
    display: flex;
    flex-direction: column;
    gap: 1rem;
    width: 100%;
    max-width: 500px;
  }

  label{
    color: #1c1b1b;
    font-size: 0.8rem;
  }

  select{
    padding: 0.8rem; 
    background: #f3f3f3;
    border: 1px solid #0e0d0d;
    outline: #080808;
    color: #171616;
    width: 100%;
    border-radius: 0.5rem;
    font-family: 'Inter';
    font-size: 0.8rem;
  }
    
  select:focus{
    outline: #111111;
    border: 1px solid #070707;
    transition: all 0.3s ease-in-out;
  }

  @media (min-width: 768px) {

      
  }

</style>
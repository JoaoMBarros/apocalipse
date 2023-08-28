<template>
    <div class="box animate__animated animate__fadeIn" style="margin: 10%; margin-left: 13%; height: auto; width: 75%;" id="app">
        <div class="column is-12" style="margin-left: 25px">
            <div style="margin-bottom: 40px; font-family: Flesh-Eating Comic Bold;">
            <h2 class="is-size-2 has-text-centered"> Adicionar sobreviventes</h2>
            </div>

            <button style="font-family: Flesh-Eating Comic Bold; margin-right: 10px;" class="button is-danger is-rounded" @click="adicionarSobrevivente">
            <span class="icon"> <i class="fas fa-biohazard"></i></span>
            <span>Novo Sobrevivente</span>
            </button>
            
            <button style="font-family: Flesh-Eating Comic Bold;" class="button is-danger is-rounded" @click="iniciar">
            <span class="icon"> <i class="fas fa-biohazard"></i></span>
            <span>Iniciar</span>
            </button>

            <div class="columns is-flex-wrap-wrap" style="margin: 0px;">
                <NovoSobrevivente v-for="(sobrevivente, index) in sobreviventes" :key="index" @excluir="excluirSobrevivente(index)" />
            </div>
        </div>
    </div>
</template>

<script>
import NovoSobrevivente from './NovoSobrevivente.vue';
import { useRoute  } from 'vue-router';

export default {
  name: 'SobreVivenciaView',
  components: {
    NovoSobrevivente,
  },
  data() {
    return {
      sobreviventes: [],
      current_url: '',
    }
  },
  methods: {
    adicionarSobrevivente() {
        this.sobreviventes.push({});
    },
    excluirSobrevivente(index) {
        this.sobreviventes.splice(index, 1);
    },
    iniciar(){
        if (this.sobreviventes.length < 2){
            alert("É necessário ter no mínimo 2 sobreviventes para iniciar o jogo")
            return
        }

        this.$router.push(`${this.current_url}/iniciar/`)
    }
  },

  created(){
        const route=useRoute();
        const path = route.path;
        console.log(path)
        this.current_url = path;
    }
}
</script>
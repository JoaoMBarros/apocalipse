<template>
    <!-- Criação de uma div que fica centralizada na tela -->
    <div class="box animate__animated animate__fadeIn" style="margin: 10%; height: auto; width: 75%;" id="app">
        <div class="column is-12" style="margin-left: 0px">
            <div style="margin-bottom: 40px; font-family: Flesh-Eating Comic Bold;">
            <h2 class="is-size-2 has-text-centered"> Adicionar sobreviventes</h2>
            </div>

            <button style="margin-right: 10px;" class="button is-danger is-rounded" @click="addNewSobrevivente">
            <span class="icon"> <i class="fas fa-biohazard"></i></span>
            <span>Novo Sobrevivente</span>
            </button>

            <button class="button is-danger is-rounded" @click="addNewSobrevivente">
            <span class="icon"> <i class="fas fa-biohazard"></i></span>
            <span>Iniciar</span>
            </button>

            <div class="columns is-flex-wrap-wrap">
                <NovoSobrevivente v-for="(sobrevivente, index) in sobreviventes" :key="index" @excluir="excluirSobrevivente(index)" />
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'
import NovoSobrevivente from './NovoSobrevivente.vue';

export default {
  name: 'SobreVivenciaView',
  components: {
    NovoSobrevivente,
  },
  data() {
    return {
      sobreviventes: [],
    }
  },
  methods: {
    addNewSobrevivente() {
      this.sobreviventes.push({});
    },
    excluirSobrevivente(index) {
      this.sobreviventes.splice(index, 1);
    },
  }
}
</script>
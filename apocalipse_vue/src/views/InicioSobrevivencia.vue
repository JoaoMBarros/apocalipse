<template>
  <div class="InicioSobrevivencia">
    <section class="hero is-medium mb-6">
      <div class="hero-body has-text-centered animate__animated animate__fadeInUp">
        <p style="font-family: Flesh-Eating Comic Bold; font-size: 100px;">
          Apocalipse
        </p>
        <button class="button is-danger is-rounded" @click="comecarAcoes">
          <span class="icon"><i class="fas fa-biohazard"></i></span>
          <span>Iniciar</span>
        </button>
        <div class="columns is-flex-wrap-wrap">
          <ListarSobreviventes :sobreviventes="this.sobreviventes"/>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
import ListarSobreviventes from './ListarSobreviventes.vue';
import { useRoute  } from 'vue-router';

export default {
    name: 'InicioSobrevivenciaView',
    components: {
        ListarSobreviventes,
    },
    data() {
        return {
            sobrevivente: {
                nome: '',
                idade: '',
                sexo: '',
                jogo_id: '',
            },
            inventario: {
                agua: '',
                comida: '',
                medicamento: '',
                municao: '',
            },
            sobreviventes: [],
            id_jogo: '',
            current_url: '',
        };
    },
    methods: {
        listarSobreviventes() {
            // Retorna a lista com os sobreviventes
            axios.get(`/sobreviventes/${this.$route.params.id}/`) 
              .then(response => {
                console.log('Resposta da requisição GET:', response.data);
                this.sobreviventes = response.data;
              })
              .catch(error => {
                console.error('Erro na requisição GET:', error);
              });
          },
          comecarAcoes(){
            this.$router.push(`/sobrevivencia/${this.$route.params.id}/acoes/`)
          }
    },
    created(){
        this.listarSobreviventes();
    }
}
</script>
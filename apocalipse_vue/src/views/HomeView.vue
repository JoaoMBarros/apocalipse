<template>
  <div class="home">
    <section class="hero is-medium mb-6">
      <div class="hero-body has-text-centered animate__animated animate__fadeInUp">
        <p class="title mb-8" style="font-family: Flesh-Eating Comic Bold; font-size: 250px;">
          Apocalipse
        </p>
        <p class="subtitle" style="font-family: Flesh-Eating Comic Bold; font-size: 60px;">
          Uma sobrevivência zumbi
        </p>
        <button class="button is-danger" style="font-family: Flesh-Eating Comic Bold" @click="iniciarSobrevivencia">
          <span class="icon"><i class="fas fa-biohazard"></i></span>
          <span>Iniciar apocalipse</span>
        </button>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HomeView',
  methods: {
    iniciarSobrevivencia() {
      axios.get('/sobreviventes/novo_jogo/') 
        .then(response => {
          console.log('Resposta da requisição GET:', response.data);
          this.$router.push(`/sobrevivencia/${response.data}`);
        })
        .catch(error => {
          console.error('Erro na requisição GET:', error);
        });
    }
  }
}
</script>
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

        <router-link to="/sobrevivencia/" class="button is-danger">
          <span class="icon"><i class="fas fa-biohazard"></i></span>
          <span>Iniciar apocalipse</span>
        </router-link>
      </div>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>

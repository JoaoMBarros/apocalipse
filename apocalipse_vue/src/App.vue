<template>
    <div>
      <nav class="navbar is-dark">
        <div class="navbar-menu">
          <div class="navbar-start">
            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/" class="button is-info">
                  <span class="icon"><i class="fas fa-home"></i></span>
                  <span>Home</span>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </nav>

    <section>
      <RouterView/>
    </section>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';
</style>

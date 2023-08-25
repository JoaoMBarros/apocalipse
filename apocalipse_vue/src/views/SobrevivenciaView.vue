<!--
    Criar uma tela de inputs de criação de sobreviventes e inventários
-->
<template>
    <!-- Criação de uma div que fica centralizada na tela -->
    <div class="box animate__animated animate__fadeIn" style="margin: 10%; height: 250px; width: 75%;">
        <div class="column is-12" style="margin-left: 0px">
            <div style="font-family: Flesh-Eating Comic Bold;">
                <h2 class="is-size-2 has-text-centered"> Adicionar sobreviventes </h2>
                <br>
                <!-- Criação dos inputs para nome, idade e sexo-->
                <label class="label">NOME <input type="text" name="nome"></label>
                <label class="label">IDADE <input type="text" name="idade"></label>
                <label class="label">SEXO <input type="text" name="sexo"></label>
            </div>
        </div>
    </div>              
</template>


<style lang="scss">
@import 'bulma';
</style>
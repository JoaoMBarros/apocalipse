<template>
    <div v-for="(sobrevivente, index) in sobreviventes" :key="index" class="box has-background-white-ter animate__animated animate__fadeIn" style="width: 25%; font-family: Flesh-Eating Comic Bold; margin: 45px;">
        <label class="is-size-5">
          <span v-if="!mostrarInventario[sobrevivente.id]?.mostrarInventario">
            <strong>Nome:</strong> {{ sobrevivente.nome }}<br>
            <strong>Idade:</strong> {{ sobrevivente.idade }}<br>
            <strong>Sexo:</strong> {{ sobrevivente.sexo }}
          </span>
          <span v-if="mostrarInventario[sobrevivente.id]?.mostrarInventario">
            <strong>Agua:</strong> {{ mostrarInventario[sobrevivente.id].inventario.agua }}<br>
            <strong>Comida:</strong> {{ mostrarInventario[sobrevivente.id].inventario.comida }}<br>
            <strong>Medicamento:</strong> {{ mostrarInventario[sobrevivente.id].inventario.medicamento }}<br>
            <strong>Munição:</strong> {{ mostrarInventario[sobrevivente.id].inventario.municao }}<br>
          </span>
        </label>

        <div class="has-text-centered" style="margin-top: 10px">
            <button class="button is-primary is-rounded" style="font-family: Flesh-Eating Comic Bold;" @click="buscarInventario(sobrevivente.id)">
                {{ mostrarInventario[sobrevivente.id]?.mostrarInventario ? 'Voltar' : 'Inventário' }}
            </button>            
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default{
    props: {sobreviventes: 'sobreviventes'},
    name: 'ListarSobreviventes',
    components: {
    },
    data() {
    return {
        mostrarInventario: {}
    };
    },
    methods: {
    buscarInventario(sobrevivente_id) {
        if (!this.mostrarInventario[sobrevivente_id]?.mostrarInventario) {
            axios.get(`/sobreviventes/${sobrevivente_id}/inventario/`)
            .then(response => {
                console.log('Resposta da requisição GET:', response.data);
                // Armazenar inventário em um objeto separado para o sobrevivente
                this.mostrarInventario[sobrevivente_id] = {
                mostrarInventario: !this.mostrarInventario[sobrevivente_id]?.mostrarInventario,
                inventario: response.data
                };
            })
            .catch(error => {
                console.error('Erro na requisição GET:', error);
            });
        } else {
        // Voltar para as informações do sobrevivente
        this.mostrarInventario[sobrevivente_id].mostrarInventario = false;
      }
    }
    }
}
</script>
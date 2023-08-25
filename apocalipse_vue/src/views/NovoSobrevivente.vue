<template>
    <div class="box animate__animated animate__fadeIn" style="width: 25%; font-family: Flesh-Eating Comic Bold; margin: 45px;">
      <template v-if="!mostrarInventario">
        <label>Nome: <input class="input" type="text" v-model="sobrevivente.nome"></label>
        <label>Idade: <input class="input" type="number" v-model="sobrevivente.idade"></label>
        <label>Sexo: <input class="input" type="text" v-model="sobrevivente.sexo"></label>
        
        <button style="margin-top: 10px;" class="button is-primary is-rounded" @click="toggleInventario()">
          {{ mostrarInventario ? 'Voltar' : 'Inventário' }}
        </button>

        <button style="margin-top: 10px; " class="button is-danger is-rounded" @click="excluirSobrevivente()">Excluir</button>
      </template>
  
      <template v-else>
        <label>Água: <input class="input" type="number" v-model="inventario.agua"></label>
        <label>Comida: <input class="input" type="number" v-model="inventario.comida"></label>
        <label>Medicamento: <input class="input" type="number" v-model="inventario.medicamento"></label>
        <label>Munição: <input class="input" type="number" v-model="inventario.municao"></label>
        
        <div style="margin-top: 10px;">
          <button class="button is-success is-rounded" @click="enviarDados()">Enviar Dados</button>
          <button class="button is-danger is-rounded" @click="cancelarInventario()">Voltar</button>
        </div>
      </template>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { useRoute } from 'vue-router';

  export default {
    name: 'NovoSobrevivente',
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
        mostrarInventario: false,
        routeId: null,
      };
    },
    methods: {
    // Função que altera a div para mostrar o inventário
      toggleInventario() {
        this.mostrarInventario = !this.mostrarInventario;
      },

    // Função que envia os dados do sobrevivente e do inventário para a API
      enviarDados() {
        if (this.mostrarInventario) {
          // Enviar dados de sobrevivente e inventário
          const jsonData = {
            sobrevivente: this.sobrevivente,
            inventario: this.inventario
          };
  
          axios.post('/sobreviventes/', jsonData)
            .then(response => {
              console.log('Dados enviados:', response.data);
              this.mostrarInventario = false;
            })
            .catch(error => {
              console.error('Erro ao enviar dados:', error);
            });
        } else {
          this.mostrarInventario = true;
        }
      },
    
    // Função de voltar para as informações de sobrevivente
      cancelarInventario() {
        this.mostrarInventario = false;
      },

    // Função que exclui o sobrevivente
      excluirSobrevivente() {
            this.$emit('excluir');
      },
    },

    // Pegando o id do jogo após o componente ser criado
    created() {
        const router = useRoute();
        this.sobrevivente.jogo_id = router.params.id;
        console.log(this.routeId);
    },

  };
  </script>
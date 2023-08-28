<template>
    <div class="box has-background-white-ter animate__animated animate__fadeIn" style="width: 25%; font-family: Flesh-Eating Comic Bold; margin: 45px;">
      <template v-if="!mostrarInventario">
        <label>Nome: <input class="input" type="text" v-model="sobrevivente.nome"></label>
        <label>Idade: <br><input style="width: 25%" class="input" type="number" v-model="sobrevivente.idade"></label>
        <div class="select is-multiple" style="width: 100%">
          Sexo:
          <select @change="muda($event)">
            <option value="" disabled selected>Selecione</option>
            <option value="M">Masculino</option>
            <option value="F">Feminino</option>
          </select>
        </div>
        
        <button style="margin-top: 10px; margin-right: 10px; font-family: Flesh-Eating Comic Bold;" class="button is-primary is-rounded" @click="toggleInventario()">Inventário</button>
        <button style="margin-top: 10px; font-family: Flesh-Eating Comic Bold;" class="button is-danger is-rounded" @click="excluirSobrevivente()">Excluir</button>
      </template>
  
      <template v-else>
        <label>Água: <input class="input" type="number" v-model="inventario.agua"></label>
        <label>Comida: <input class="input" type="number" v-model="inventario.comida"></label>
        <label>Medicamento: <input class="input" type="number" v-model="inventario.medicamento"></label>
        <label>Munição: <input class="input" type="number" v-model="inventario.municao"></label>
        
        <div style="margin-top: 10px;">
          <button class="button is-success is-rounded" style="font-family: Flesh-Eating Comic Bold;" @click="enviarDados()">Criar</button>
          <button class="button is-danger is-rounded" style="font-family: Flesh-Eating Comic Bold;" @click="cancelarInventario()">Voltar</button>
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
      muda(event) {
        this.sobrevivente.sexo = event.target.value;
      },

    // Função que envia os dados do sobrevivente e do inventário para a API
      enviarDados() {
        if (this.mostrarInventario) {
          // Enviar dados de sobrevivente e inventário
          const jsonData = {
            sobrevivente: this.sobrevivente,
            inventario: this.inventario
          };

          // Checar se algum campo do sobrevivente está vazio
            for (const [key, value] of Object.entries(jsonData.sobrevivente)) {
                if (value === '') {
                alert('Preencha todos os campos de sobrevivente!');
                return;
                }
            }

          axios.post('/sobreviventes/', jsonData)
            .then(response => {
              this.mostrarInventario = false;
            })
            .catch(error => {
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
    },

  };
  </script>
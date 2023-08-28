<template>
    <div class="box has-background-white-ter animate__animated animate__fadeIn" style="width: auto; font-family: Flesh-Eating Comic Bold; margin: 45px; display: flex; justify-content: center;">
      <div class="box" style="font-size: 20px; width: 25%; margin-left: 20%;">
        <label>
          <span>
            Localização: {{ sobrevivente.latitude }}, {{ sobrevivente.longitude }}<br>
            Água: {{ inventario.agua }}<br>
            Comida: {{ inventario.comida }}<br>
            Medicamento: {{ inventario.medicamento }}<br>
            Munição: {{ inventario.municao }}
          </span>
        </label>
      </div>

        <div style="margin-left: 20px; margin-right: 20px; font-size: 19px;">

            <span v-if="acao == 'troca'">
            Sobrevivente {{ sobrevivente.nome }} quer trocar itens com {{ outro_sobrevivente.nome }}!<br>
                <div class="columns">
                    <div v-for="item in ['agua', 'comida', 'medicamento', 'municao']" :key="item" class="column is-3">
                        <label>{{ item.charAt(0).toUpperCase() + item.slice(1) }} <br>
                        <input class="input" type="number" v-model="itens[item]">
                        </label>
                    </div>
                </div>

                <div class="columns">
                    <div v-for="item in ['agua', 'comida', 'medicamento', 'municao']" :key="item" class="column is-3">
                        <label>{{ item.charAt(0).toUpperCase() + item.slice(1) }} <br>
                        <input class="input" type="number" v-model="outro_itens[item]">
                        </label>
                    </div>
                </div>
            </span>

            <span v-else>
                <label v-if="acao === 'fugiu'">
                    Sobrevivente {{ sobrevivente.nome }} quer fugir! <br>
                    Nova localização: {{ random_latitude }}, {{ random_longitude }}
                </label>
                <label v-else-if="acao === 'visto_infectado'" class="is-inline-block">Sobrevivente {{ sobrevivente.nome }} foi avistado infectado!</label>
            </span>
            </div>
  
      <div v-if="acao == 'troca'" class="box" style="width: 25%; font-size: 20px;">
            <label>
              <span>
                Localização: {{ outro_sobrevivente.latitude }}, {{ outro_sobrevivente.longitude }}<br>
                Água: {{ outro_sobrevivente_inventario.agua }}<br>
                Comida: {{ outro_sobrevivente_inventario.comida }}<br>
                Medicamento: {{ outro_sobrevivente_inventario.medicamento }}<br>
                Munição: {{ outro_sobrevivente_inventario.municao }}
              </span>
            </label>
      </div>

      <div style="display: flex; justify-content: flex-end; width:100%; margin-top: 10px;">
            <button class="button is-danger is-rounded" style="font-family: Flesh-Eating Comic Bold;" @click="recebeNovaAcao">Outra Ação</button>
            <button class="button is-primary is-rounded" style="font-family: Flesh-Eating Comic Bold; margin-right: 5px;" @click="enviaNovaAcao">Concluir ação</button>
            <button class="button is-dark is-rounded" style="font-family: Flesh-Eating Comic Bold; margin-right: 5px;" @click="finalizaSimulacao">Finalizar</button>
        </div>
    </div>
  </template>

<script>
import axios from 'axios';

export default{
    name: 'Acoes',
    data() {
        return {
            acao: [],

            sobrevivente: {
                sobrevivente: '',
                nome: '',
                idade: '',
                sexo: '',
            },

            outro_sobrevivente: {
                sobrevivente: '',
                nome: '',
                idade: '',
                sexo: '',
            },

            inventario: {
                agua: '',
                comida: '',
                medicamento: '',
                municao: '',
            },

            outro_sobrevivente_inventario: {
                agua: '',
                comida: '',
                medicamento: '',
                municao: '',
            },

            itens: {
                agua: 0,
                comida: 0,
                medicamento: 0,
                municao: 0,
            },

            outro_itens: {
                agua: 0,
                comida: 0,
                medicamento: 0,
                municao: 0,
            },

            random_latitude: '',
            random_longitude: '',
        };
    },

    methods: {
        resetaDados(){
            this.itens = {
                agua: 0,
                comida: 0,
                medicamento: 0,
                municao: 0,
            },
            this.outro_itens = {
                agua: 0,
                comida: 0,
                medicamento: 0,
                municao: 0,
            },
            this.random_latitude = '',
            this.random_longitude = ''
        },
        async recebeNovaAcao() {
            try {
                const response = await axios.get(`/sobreviventes/${this.$route.params.id}/nova_acao`);
                this.acao = response.data.acao;

                const sobreviventeResponse = await axios.get(`/sobreviventes/${response.data.sobrevivente}/`);
                this.sobrevivente = sobreviventeResponse.data;

                const inventarioResponse = await axios.get(`/sobreviventes/${response.data.sobrevivente}/inventario/`);
                this.inventario = inventarioResponse.data;

                if (this.acao === 'fugiu') {
                    this.random_latitude = this.randomFloat(-15, 15);
                    this.random_longitude = this.randomFloat(-15, 15);
                }

                if (this.acao === 'troca' || this.acao === 'visto_infectado') {
                const outroSobreviventeResponse = await axios.get(`/sobreviventes/${response.data.outro_sobrevivente}/`);
                this.outro_sobrevivente = outroSobreviventeResponse.data;

                const outroInventarioResponse = await axios.get(`/sobreviventes/${response.data.outro_sobrevivente}/inventario/`);
                this.outro_sobrevivente_inventario = outroInventarioResponse.data;
                }
            } catch (error) {
                console.error('Erro na requisição GET:', error);
            }
        },
        enviaNovaAcao() {
            let jsonData = {};
            let endpoint = '';

            if (this.acao === 'fugiu') {
                jsonData = {
                sobrevivente: this.sobrevivente.id,
                latitude: this.random_latitude,
                longitude: this.random_longitude,
                };
                endpoint = '/sobreviventes/localizacao/';
            } else if (this.acao === 'visto_infectado') {
                jsonData = {
                sobrevivente: this.sobrevivente.id,
                };
                endpoint = '/sobreviventes/infectado/';
            } else if (this.acao === 'troca') {
                jsonData = {
                troca: [
                    {
                    sobrevivente: this.sobrevivente.id,
                    itens: {
                        agua: this.itens.agua,
                        comida: this.itens.comida,
                        medicamento: this.itens.medicamento,
                        municao: this.itens.municao,
                    },
                    },
                    {
                    sobrevivente: this.outro_sobrevivente.id,
                    itens: {
                        agua: this.outro_itens.agua,
                        comida: this.outro_itens.comida,
                        medicamento: this.outro_itens.medicamento,
                        municao: this.outro_itens.municao,
                    },
                    },
                ],
                };
                endpoint = '/sobreviventes/troca/';
            }

            const requestConfig = {
                method: this.acao === 'troca' ? 'post' : 'patch',
                url: endpoint,
                data: jsonData,
            };

            console.log(requestConfig)
            
            axios(requestConfig)
                .then(response => {
                    this.recebeNovaAcao();
                    this.resetaDados();
                })
                .catch(error => {
                alert(error.response.data)
                });
        },
        finalizaSimulacao(){
            this.$router.push(`/sobrevivencia/${this.$route.params.id}/relatorio/`)
        },
        // Gera um numero float aleatório
        randomFloat(min, max) {
            return Math.random() * (max - min) + min;
        }
    },
    created(){
        this.recebeNovaAcao()
    }
}
</script>
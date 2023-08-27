<template>
    <div class="box has-background-white-ter animate__animated animate__fadeIn" style="width: auto; font-family: Flesh-Eating Comic Bold; margin: 45px; display: flex; justify-content: center;">
      <div class="box" style="width: 20%; margin-left: 20%;">
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

        <span v-if="acao == 'troca'" style="margin-top: 50px; margin-left: 20px; margin-right: 20px;">
          Sobrevivente {{ sobrevivente.nome }} quer trocar inventário com {{ outro_sobrevivente.nome }}!<br>
        </span>
        <span v-else style="margin-top: 50px; margin-left: 20px; margin-right: 20px">
          <label v-if="acao === 'fugiu'">Sobrevivente {{ sobrevivente.nome }} quer fugir!</label>
          <label v-else-if="acao === 'visto_infectado'">Sobrevivente {{ sobrevivente.nome }} foi avistado infectado!</label>
        </span>
  
      <div v-if="acao == 'troca'" class="box" style="width: 20%;">
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

        <div style="margin-top: auto; margin-left: auto;">
            <button class="button is-primary is-rounded" style="font-family: Flesh-Eating Comic Bold;">Ação Concluída</button>
            <button class="button is-primary is-rounded" style="font-family: Flesh-Eating Comic Bold;">Outra Ação</button>
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


            random_latitude: '',
            random_longitude: '',
        };
    },

    methods: {
        async recebeNovaAcao() {
            try {
                const response = await axios.get(`/sobreviventes/${this.$route.params.id}/nova_acao`);
                this.acao = response.data.acao;

                const sobreviventeResponse = await axios.get(`/sobreviventes/${response.data.sobrevivente}/`);
                this.sobrevivente = sobreviventeResponse.data;

                const inventarioResponse = await axios.get(`/sobreviventes/${response.data.sobrevivente}/inventario/`);
                this.inventario = inventarioResponse.data;

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
        enviaNovaAcao(){
            if (this.acao == 'fugiu'){
                const jsonData = {
                    sobrevivente: this.sobrevivente.id,
                    latitude: this.sobrevivente.latitude,
                    longitude: this.sobrevivente.longitude,
                };

                axios.patch('/sobreviventes/localizacao/', jsonData)

            } else if (this.acao == 'avistou_infectado'){
                const jsonData = {
                    sobrevivente: this.sobrevivente.id,
                };

                axios.patch('/sobreviventes/localizacao/', jsonData)

            } else if (this.acao == 'trocou_inventario'){
                const jsonData = {
                    troca: [
                        {
                            sobrevivente: this.sobrevivente.id,
                            itens: {
                                agua: this.inventario.agua,
                                comida: this.inventario.comida,
                                medicamento: this.inventario.medicamento,
                                municao: this.inventario.municao,
                            }
                        },
                        {
                            sobrevivente: this.outro_sobrevivente.id,
                            itens: {
                                agua: this.outro_sobrevivente.agua,
                                comida: this.outro_sobrevivente.comida,
                                medicamento: this.outro_sobrevivente.medicamento,
                                municao: this.outro_sobrevivente.municao,
                            }
                        }
                    ]
                };

                axios.post('/sobreviventes/troca/', jsonData)
            }
        },
        getRandomArbitrary(min, max) {
            return Math.random() * (max - min) + min;
        }

    },
    created(){
        this.recebeNovaAcao()
    }
}
</script>
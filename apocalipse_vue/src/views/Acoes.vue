<template>
    <div class="box has-background-white-ter animate__animated animate__fadeIn" style="width: 50%; font-family: Flesh-Eating Comic Bold; margin: 45px; display: flex; justify-content: center;">
        <div style="width: 50%; text-align: left;">
            <div class="box" style="margin: 5px; padding: 10px;">
                <label>
                    <span>
                    Localização:
                    Água:
                    Comida:
                    Medicamento:
                    Munição:
                    </span>
                </label>
    
                <span>
                    <span>
                    Sobrevivente {{ sobrevivente.nome }} quer trocar inventário com {{ outro_sobrevivente }}!<br>
                    <div class="box" style="margin-top: 10px;">
                        <label>
                        <span>
                            Localização:
                            Água:
                            Comida:
                            Medicamento:
                            Munição:
                        </span>
                        </label>
                    </div>
                </span>
                </span>
                <span v-if="acao == 'oii'">
                    <label v-if="acao === 'fugiu'">Sobrevivente {{ sobrevivente.nome }} quer fugir!</label>
                    <label v-else-if="acao === 'infectado'">Sobrevivente {{ sobrevivente.nome }} foi avistado infectado!</label>
                </span>
            </div>
        </div>
      
            <div style="width: 50%; text-align: center;">
                <div class="box" style="margin: 5px; padding: 10px;">
                    <label>Ação: {{ acao }}</label>
                </div>
            </div>
      
    </div>
</template>

<script>
import axios from 'axios';

export default{
    name: 'Acoes',
    data() {
        return {
            acao: {
            sobrevivente: {
                id: '',
                nome: '',
                idade: '',
                sexo: '',
                jogo_id: '',
            },
            outro_sobrevivente: {
                id: '',
                nome: '',
                idade: '',
                sexo: '',
                jogo_id: '',
            }},
            inventario: {
                agua: '',
                comida: '',
                medicamento: '',
                municao: '',
            },
            routeId: null,
        };
    },

    methods: {
        recebeNovaAcao(){
            axios.get(`/sobreviventes/${this.$route.params.id}/nova_acao`)
            .then(response => {
                console.log('Resposta da requisição GET:', response.data);
                this.sobrevivente = response.data;
            })
            .catch(error => {
                console.error('Erro na requisição GET:', error);
            });
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
    },
    created(){
        this.recebeNovaAcao()
    }
}
</script>
<template>
    <div class="box animate__animated animate__fadeIn" style="margin: 10%; margin-left: 13%; height: auto; width: 75%;">
        <div class="column is-12" style="margin-left: 0px">
            <div style="margin-bottom: 40px; font-family: Flesh-Eating Comic Bold;">
                <h2 class="is-size-2 has-text-centered">Relatório de Sobreviventes</h2>
            </div>
            
            <div class="box" style="display: flex; justify-content: center; font-family: Flesh-Eating Comic Bold; font-size: large;">
                <div class="columns">
                    <span style="text-align: left; flex: 1;">
                        Porcentagem de sobreviventes infectados: {{ relatorio.porcentagem_sobreviventes_infectados }}%
                        Porcentagem de sobreviventes não infectados: {{ relatorio.porcentagem_sobreviventes_nao_infectados }}%<br>
                        Pontos perdidos devido a sobreviventes infectados: {{ relatorio.pontos_perdidos }}
                    </span>
                    <span style="text-align: center; flex: 1;">
                        <div style="text-align: center;">
                            Média de itens por sobrevivente vivo
                            <ul>
                                <li v-for="(value, key) in relatorio.quantidade_media_itens_nao_infectados" :key="key">
                                    {{ key.charAt(0).toUpperCase() + key.slice(1) }}: {{ value }}
                                </li>
                            </ul>
                        </div>
                    </span>
                    <span style="text-align: center; flex: 1;">
                        <div style="text-align: center;">
                            Itens perdidos por sobreviventes infectados
                            <ul>
                                <li v-for="(value, key) in relatorio.quantidade_itens_perdidos" :key="key">
                                    {{ key.charAt(0).toUpperCase() + key.slice(1) }}: {{ value }}
                                </li>
                            </ul>
                        </div>
                    </span>
                </div>
            </div>
        </div>
        <button class="button is-danger is-rounded" style="font-family: Flesh-Eating Comic Bold;" @click="iniciarNovaSimulacao">Nova Simulação</button>
    </div>
</template>

<script>
import axios from 'axios';
import HomeView from './HomeView.vue';

export default {
    name: 'RelatorioFinal',
    components: {
        HomeView
    },
    data() {
        return {
            relatorio: '',
        };
    },

    methods : {
        iniciarNovaSimulacao(){
            axios.get('/sobreviventes/novo_jogo/') 
            .then(response => {
                console.log('Resposta da requisição GET:', response.data);
                this.$router.push(`/sobrevivencia/${response.data}`);

                this.deletaSimulacaoAtual();
            })
            .catch(error => {
                console.error('Erro na requisição GET:', error);
            });
        },
        deletaSimulacaoAtual(){
            axios.delete(`/sobreviventes/${this.$route.params.id}/deletar`)
            .then(response => {
                console.log('Resposta da requisição DELETE:', response.data);
            })
            .catch(error => {
                console.error('Erro na requisição DELETE:', error);
            });
        }
    },
    created(){
        axios.get(`/sobreviventes/${this.$route.params.id}/relatorio`)
        .then(response => {
            console.log('Resposta da requisição GET:', response.data);
            this.relatorio=response.data;
        })
    },
    
}


</script>
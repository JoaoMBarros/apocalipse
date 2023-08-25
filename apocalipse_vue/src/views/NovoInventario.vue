<template>
    <div class="box" style= "width: 25%; font-family: Flesh-Eating Comic Bold; margin: 45px;">
        <label>Água: <input class="input is-primary" type="text" v-model="nome"></label>
        <label>Comida: <input class="input is-primary" type="text" v-model="idade"></label>
        <label>Medicamento: <input class="input is-primary" type="text" v-model="sexo"></label>
        <label>Munição: <input class="input is-primary" type="text" v-model="sexo"></label>
        <button style="margin-top: 10px;" class="button is-primary" @click="criarInventario()">Adicionar</button>
    </div>
</template>

<script>
export default {
    name: 'NovoInventario',
    data() {
        return {
            agua:'',
            comida:'',
            medicamento:'',
            municao:''
        };
    },
    methods: {
        criarInventario() {
        }
    }
}
</script>
<template>
    <div id="main">
        <b-container>
            <b-row><h5>Sqrt</h5></b-row>
            <b-row>
                <b-col sm="3"><b-form-input v-model="text" placeholder="Enter a real number"></b-form-input></b-col>
                <b-col sm="3"><b-button @click="out">Click</b-button></b-col>
            </b-row>
            <b-row>
                <div>Value: {{ output }}</div>
            </b-row>
        </b-container>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                text: '',
                output: ''
            }
        },
        methods: {
            out() {
                this.output = Math.sqrt(this.text);
            }
        },
    }
</script>

<style>

</style>
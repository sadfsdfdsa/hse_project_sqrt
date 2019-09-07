<template>
    <div>
        <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom box-shadow">
            <b-navbar-brand class="my-0 mr-md-auto font-weight-normal" :to="{name: 'indexPage'}">
                Sqrt App
            </b-navbar-brand>
            <nav class="my-2 my-md-0 mr-md-3">
                <b-row>
                    <b-form-radio-group
                            id="btn-radios-2"
                            v-model="lang"
                            :options="options"
                            buttons
                            button-variant="outline-primary"
                            size="md"
                            name="radio-btn-outline"
                    ></b-form-radio-group>
                </b-row>
            </nav>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Navigation",
        data() {
            return {
                lang: 'ru',
                options: [
                    {text: 'Ru', value: 'ru'},
                    {text: 'En', value: 'en'},
                    {text: 'Es', value: 'es'},
                    {text: '中国', value: 'ch'},
                ],
            }
        },
        watch: {
            lang: function (val) {
                this.$store.commit('change_lang', val)
            },
        }
    }
</script>

<style scoped>
    .px-md-4 {
        padding-left: 1.5rem !important;
    }

    .px-md-4 {
        padding-right: 1.5rem !important;
    }

    .p-3 {
        padding: 1rem !important;
    }

    .mb-3 {
        margin-bottom: 1rem !important;
    }
</style>

<template>
    <div id="main" class="vertical-center">
        <b-container class="text-center">
            <!--<b-row align-h="center"><h3>Sqrt</h3></b-row>-->
            <!-- Input form -->
            <b-row align-h="center">
                <b-col sm="3">
                    <b-form-input class="text-center" size="lg" v-model="text"
                                  :placeholder="dict.enter_number[lang]"></b-form-input>
                </b-col>
            </b-row>
            <!-- Output form -->
            <b-row align-h="center">
                <b-col sm="3">
                    <p class="form-control form-control-lg" :placeholder="dict.result[lang]" readonly>
                        {{ output }}
                    </p>
                </b-col>
            </b-row>
            <!-- Result button -->
            <b-row align-h="center">
                <b-col sm="3">
                    <b-button size="lg" variant="success" @click="out">{{dict.result_button[lang]}}</b-button>
                </b-col>
            </b-row>
            <!-- Divider line -->
            <b-row class="dropdown-divider"></b-row>
            <!-- Contact modal frame button -->
            <b-row align-h="center" class="mt-3">
                <b-col sm="3">
                    <b-button v-b-modal.modal_frame variant="secondary">
                        <b-row>
                            <b-col sm="12"><h6>{{dict.find_error[lang]}}</h6></b-col>
                        </b-row>
                        <b-row>
                            <b-col sm="12">
                                <div>{{dict.find_error_sub[lang]}}</div>
                            </b-col>
                        </b-row>
                    </b-button>
                    <b-modal id="modal_frame" :title="dict.modal_form_title[lang]">
                        <p class="my-4">Here email form or something like that</p>
                    </b-modal>
                </b-col>
            </b-row>
            <!-- Version row -->
            <b-row>
                <b-col sm="1"><p class="font-weight-light">1.0 stable</p></b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
    import {mapState} from 'vuex';

    export default {
        data() {
            return {
                text: '', // input
                output: '', // output var
                dict: {
                    result_button: {ru: 'Вычислить корень', en: 'Get square root'},
                    select_language: {ru: 'Выберите язык', en: 'Select language'},
                    enter_number: {ru: 'Введите число', en: 'Enter a number'},
                    result: {ru: 'Ответ', en: 'Result'},
                    do_correct_input: {
                        ru: 'Введите число',
                        en: 'Input a number'
                    },
                    find_error: {ru: 'Нашли ошибку?', en: 'Find error?'},
                    find_error_sub: {ru: 'Свяжитесь с нами', en: 'Contact us'},
                    modal_form_title: {ru: 'Обратная связь', en: 'Contact form'}
                }, // dict for en and ru langs
            }
        },
        methods: {
            out() {
                let tmp = this.sqrt_func(this.text);
                if (tmp !== 'error') {
                    // print result
                    this.output = tmp.toString();
                } else {
                    // tmp === 'error'
                    // print error message
                    this.output = this.dict.do_correct_input[this.lang]
                }
            },
            sqrt_func(number) {
                // валидация пустых строк;
                if (/^ *$/.test(number)) {
                    return 'error';
                }
                // валидация 0;
                if (number == 0) {
                    return 0;
                }
                // валидация отрицательных чисел;
                if (number < 0) {
                    return Math.sqrt(Math.abs(number)) + 'i'
                }
                // валидация положительных чисел;
                return Math.sqrt(number) || 'error';
            },
        },
        computed: mapState([
            'lang' // detecting global VueX variable LANG from Navigation
        ])
    }
</script>

<style>
    .vertical-center {
        min-height: 70%;
        min-height: 70vh;
        display: flex;
        align-items: center;
    }
</style>
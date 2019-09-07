<template>
    <div id="main" class="vertical-center">
        <b-container class="text-center">
            <b-row align-h="center"><h5>{{dict.user_guide[lang]}}</h5></b-row>
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
                    <b-modal id="modal_frame" :title="dict.modal_form_title[lang]" @ok="handle_ok">
                        <b-row>
                            <b-col class="text-center"><p class="my-4">{{dict.modal_from_text[lang]}}</p></b-col>
                        </b-row>
                        <b-row align-h="center">
                            <b-col sm="12">
                                <b-form-textarea id="textarea-default" v-model="send_error"></b-form-textarea>
                            </b-col>
                        </b-row>
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
                send_error: '',
                // dict for langs
                dict: {
                    user_guide: {
                        ru: 'юзер гайд',
                        en: 'user guide',
                        es: 'guía del usuario',
                        ch: '用户指南'
                    },
                    result_button: {
                        ru: 'Вычислить корень',
                        en: 'Get square root',
                        es: 'Calcular raíz',
                        ch: '得到平方根'
                    },
                    enter_number: {
                        ru: 'Введите число',
                        en: 'Enter a number',
                        es: 'Ingrese un número',
                        ch: '输入号码'
                    },
                    result: {
                        ru: 'Ответ',
                        en: 'Result',
                        es: 'La respuesta',
                        ch: '结果'
                    },
                    do_correct_input: {
                        ru: 'Введите число',
                        en: 'Input a number',
                        es: 'Ingrese un número',
                        ch: '输入号码'
                    },
                    find_error: {
                        ru: 'Нашли ошибку?',
                        en: 'Find error?',
                        es: '¿Encontró un error?',
                        ch: '发现错误？'
                    },
                    find_error_sub: {
                        ru: 'Свяжитесь с нами',
                        en: 'Contact us',
                        es: 'Contáctenos',
                        ch: '联系我们'
                    },
                    modal_form_title: {
                        ru: 'Обратная связь',
                        en: 'Contact form',
                        es: 'Formulario de contacto',
                        ch: '联系表'
                    },
                    modal_from_text: {
                        ru: 'текст',
                        en: 'text',
                        es: 'text es',
                        ch: '文本'
                    }
                },
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
            handle_ok() {
                this.$api.post("/error", {text: this.send_error})
                    .then(({data}) => {
                        this.$snotify.success('Complete!')
                    })
                    .catch(e => {
                        this.$snotify.error(`Error status ${e.response.status}`);
                    });
                this.send_error = '';
            },
            sqrt_func(number) {
                // валидация пустых строк;
                if (/^ *$/.test(number)) {
                    return 'error';
                }
                // валидация sin cos tg ctg;
                if (number.startsWith('cos') || number.startsWith('sin') ||
                    number.startsWith('tg') || number.startsWith('ctg')
                ) {
                    // переопределение дефолтных функций для tg и ctg;
                    Math.tg = Math.tan;
                    Math.ctg = function (value) {
                        return 1 / Math.tan(value)
                    };
                    // парсинг и нахождение числового значения тригонометрических параметров;
                    number = Math[number.match(/^(cos|sin|tg|ctg)/g)[0]](number.match(/[-]{0,1}[\d]*[\.]{0,1}[\d]+/g)[0]);
                }
                // валидация 0;
                if (number == 0) {
                    return 0;
                }
                // валидация отрицательных чисел;
                if (number < 0) {
                    return '±' + Math.sqrt(Math.abs(number)) + 'i' || 'error';
                }
                // валидация положительных чисел;
                return '±' + Math.sqrt(number) || 'error';
            },
        }
        ,
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
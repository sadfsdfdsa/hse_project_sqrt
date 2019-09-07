<template>
    <div id="main" class="vertical-center">
        <b-container class="text-center">
            <b-row align-h="center"><h5>{{dict.user_guide_h[lang]}}</h5></b-row>
            <b-row align-h="center"><p>{{dict.user_guide[lang]}}</p></b-row>
            <!-- Input form -->
            <b-row align-h="center">
                <b-col sm="3">
                    <b-form-input class="text-center" size="lg" v-model="text"
                                  :placeholder="dict.enter_number[lang]"></b-form-input>
                </b-col>
            </b-row>
            <!-- Output place -->
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
                    <b-modal id="modal_frame" :title="dict.modal_frame_title[lang]" hide-footer>
                        <b-row class="h-25">
                            <b-col class="text-center"><h5 class="my-4">{{dict.modal_frame_text[lang]}}</h5></b-col>
                        </b-row>
                        <b-row align-h="center">
                            <b-col sm="12">
                                <b-form-textarea id="textarea-default" v-model="send_error"></b-form-textarea>
                            </b-col>
                        </b-row>
                        <b-row class="h-25">
                            <b-col class="text-center"><p class="my-4">{{dict.modal_frame_text_sub[lang]}}
                            <a href="mailto:akshuvaev@edu.hse.ru" target="_blank" class="btn btn-primary">akshuvaev@edu.hse.ru</a></p></b-col>
                        </b-row>
                        <b-button class="mt-3" block @click="$bvModal.hide('modal_frame')">
                            {{dict.cancel_button[lang]}}
                        </b-button>
                        <b-button class="mt-3" variant="primary" block
                                  @click="$bvModal.hide('modal_frame'); submit()">
                            {{dict.submit_button[lang]}}
                        </b-button>
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
                // dict for translate to Russian. English, Spanish, Chinese
                dict: {
                    user_guide_h: {
                        ru: 'Вычисление квадратного корня',
                        en: 'Square root calculation',
                        es: 'Cálculo de raíz cuadrada',
                        ch: '平方根计算'
                    },
                    user_guide: {
                        ru: 'Введите значение от -10^309 до 10^309 или тригонометрическую функцию с радианами: cos(1), например.',
                        en: 'Enter a value from -10^309 to 10^309 or a trigonometric function with radians, for example: cos(1).',
                        es: 'Ingrese un valor de -10^309 a 10^309 o una función trigonométrica con radianes, por ejemplo: cos(1).',
                        ch: '输入-10^309到10^309的值或带弧度的三角函数，例如：cos(1）。'
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
                    modal_frame_title: {
                        ru: 'Обратная связь',
                        en: 'Contact form',
                        es: 'Formulario de contacto',
                        ch: '联系表'
                    },
                    modal_frame_text: {
                        ru: 'Опишите вашу проблему',
                        en: 'Describe your problem',
                        es: 'Describe tu problema',
                        ch: '描述你的问题'
                    },
                    modal_frame_text_sub: {
                        ru: 'Или напишите нам на почту:',
                        en: 'Or write to us by mail:',
                        es: 'O escríbanos por correo:',
                        ch: '或者通过邮件写信给我们'
                    },
                    submit_button: {
                        ru: 'Отправить',
                        en: 'Submit',
                        es: 'Enviar',
                        ch: '提交'
                    },
                    cancel_button: {
                        ru: 'Отмена',
                        en: 'Cancel',
                        es: 'Cancelar',
                        ch: '取消'
                    },
                },
            }
        },
        methods: {
            out() {
                let tmp = this.sqrt_func(this.text);
                if (tmp !== 'error') {
                    // print result
                    if (tmp != 0) {
                        this.output = '±' + tmp.toString();
                    } else {
                        this.output = tmp.toString()
                    }
                } else {
                    // tmp === 'error'
                    // print error message
                    this.output = this.dict.do_correct_input[this.lang]
                }
            },
            submit() {
                if (this.send_error) {
                    // Отправка текста на /api/v1/error, где она хранится и предоставляется по GET запросу /api/v1/error;
                    this.$api.post("/error", {text: this.send_error})
                        .then(({data}) => {
                            this.$snotify.success('Complete!')
                        })
                        .catch(e => {
                            this.$snotify.error(`Error status ${e.response.status}`);
                        });
                    this.send_error = '';
                }
            },
            sqrt_func(number) {
                // валидация пустых строк;
                if (/^ *$/.test(number)) {
                    return 'error';
                }
                // валидация sin cos tg ctg;
                if (number.startsWith('cos(') || number.startsWith('sin(') ||
                    number.startsWith('tg(') || number.startsWith('ctg(')
                ) {
                    // переопределение дефолтных функций для tg и ctg;
                    Math.tg = Math.tan;
                    Math.ctg = function (value) {
                        return 1 / Math.tan(value)
                    };
                    // парсинг и нахождение числового значения тригонометрических параметров;
                    number = Math[number.match(/^(cos|sin|tg|ctg)/g) || NaN](number.match(/[-]{0,1}[\d]*[\.]{0,1}[\d]+/g) || NaN);
                }
                // валидация 0;
                if (number == 0) {
                    return 0;
                }
                // валидация отрицательных чисел;
                if (number < 0) {
                    return Math.sqrt(Math.abs(number)) + 'i' || 'error';
                }
                // валидация положительных чисел;
                return Math.sqrt(number) || 'error';
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
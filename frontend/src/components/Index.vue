<template>
    <div id="main">
        <b-container>
            <b-row><h5>Sqrt</h5></b-row>
            <b-row>
                <b-col sm="3">
                    <b-form-input v-model="text" :placeholder="dict.enter_number[lang]"></b-form-input>
                </b-col>
                <b-col sm="3">
                    <b-button variant="success" @click="out">{{dict.result_button[lang]}}</b-button>
                </b-col>
            </b-row>
            <b-row class="mb-3">
                <b-col sm="3">
                    <b-form-input :placeholder="output" disabled>{{dict.result[lang]}}: {{
                        output }}
                    </b-form-input>
                </b-col>
            </b-row>
            <b-row class="dropdown-divider"></b-row>
            <b-row class="mt-3">
                <b-col sm="3">
                    <b-button variant="info" @click="do_tests">{{dict.run_tests[lang]}}</b-button>
                </b-col>
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
            <div v-if="passed">
                <b-row><label><h5>{{dict.done_tests[lang]}}</h5></label></b-row>
                <b-progress class="mt-2" :max="tests.length" show-value>
                    <b-progress-bar :value="passed" variant="success"></b-progress-bar>
                    <b-progress-bar :value="tests.length-passed" variant="danger"></b-progress-bar>
                </b-progress>
                <b-table hover :items="tests"></b-table>
                <b-row>{{dict.comment_for_tests[lang]}}</b-row>
            </div>
        </b-container>
    </div>
</template>

<script>
    import {mapState} from 'vuex';

    export default {
        data() {
            return {
                passed: NaN,
                text: '',
                output: '',
                dict: {
                    result_button: {ru: 'Вычислить корень', en: 'Get square root'},
                    select_language: {ru: 'Выберите язык', en: 'Select language'},
                    enter_number: {ru: 'Введите положительное число', en: 'Enter a real number'},
                    result: {ru: 'Ответ', en: 'Result'},
                    run_tests: {ru: 'Запустить тесты!', en: 'Run tests!'},
                    do_correct_input: {
                        ru: 'Введите положительное число',
                        en: 'Input correct real number'
                    },
                    done_tests: {ru: 'Завершенные тесты:', en: 'Completed tests:'},
                    comment_for_tests: {
                        ru: 'Последние два теста включают в себя пустые строки с 1 и множественными пробелами.',
                        en: 'Last 2 tests included 1 and more spaces in empty strings.'
                    },
                    find_error: {ru: 'Нашли ошибку?', en: 'Find error?'},
                    find_error_sub: {ru: 'Свяжитесь с нами', en: 'Contact us'},
                    modal_form_title: {ru: 'Обратная связь', en: 'Contact form'}
                },
                options: [
                    {text: 'Ru', value: 'ru'},
                    {text: 'En', value: 'en'},
                ],
                tests: [
                    {input: 4, output: NaN, correct: 2, _rowVariant: 'danger'},
                    {input: 1, output: NaN, correct: 1, _rowVariant: 'danger'},
                    {input: 0, output: NaN, correct: 0, _rowVariant: 'danger'},
                    {input: -4, output: NaN, correct: 'error', _rowVariant: 'danger'},
                    {input: 'string example', output: NaN, correct: 'error', _rowVariant: 'danger'},
                    {input: '', output: NaN, correct: 'error', _rowVariant: 'danger'},
                    {input: '   ', output: NaN, correct: 'error', _rowVariant: 'danger'},
                    {input: 'example error test!', output: NaN, correct: 'incorrect example!', _rowVariant: 'danger'},
                ],
            }
        },
        methods: {
            out() {
                let tmp = this.sqrt_func(this.text);
                if (tmp !== 'error') {
                    this.output = tmp.toString();
                } else {
                    this.output = this.dict.do_correct_input[this.lang]
                }
            },
            do_tests() {
                if (!this.passed) {
                    let tested_func = this.sqrt_func;
                    let passed = 0;
                    this.tests.forEach(function (item) {
                        item.output = tested_func(item.input);
                        if (item.correct === item.output) {
                            passed += 1;
                            item._rowVariant = 'success';
                        } else {
                            item._rowVariant = 'danger';
                        }
                    });
                    this.passed = passed;
                } else {
                    this.passed = NaN;
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
                return Math.sqrt(number) || 'error';
            },
        },
        computed: mapState([
            'lang'
        ])
    }
</script>

<style>

</style>
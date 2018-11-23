import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex);

import course from "./course.js"
import account from "./account.js"

export default new Vuex.Store({
    modules: {
        course,
        account
    }
})
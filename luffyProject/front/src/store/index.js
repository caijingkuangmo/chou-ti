import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex);

import course from "./course.js"

export default new Vuex.Store({
    modules: {
        course,
    }
})
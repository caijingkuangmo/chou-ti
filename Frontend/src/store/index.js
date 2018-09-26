import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

import user from './modules/user.js'
import actions from './actions.js'


export default new Vuex.Store({
    actions,
    modules: {
        user
    }
});
const state = {
    count:6,
}

var getters = {
    count(state) {
        return state.count;
    }
}

const actions = {
    increment({ commit, state }) {

    }
}

const mutations = {
    increment(state){

    }
}

export default {
    state,
    getters,
    actions,
    mutations
}


const state = {
    count: 6
}

var getters = {
    count(state) {
        return state.count;
    }
}

const mutations = {
    increment(state) {
        state.count++;
    }
}

const actions = {
    increment({ commit, state }) {
        commit("increment");
    }
}


export default {
    state,
    getters,
    actions,
    mutations
}
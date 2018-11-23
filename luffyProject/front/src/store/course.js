import axios from "axios";
import config from "@/config/config.js"

const state = {
    courseList: []
}

var getters = {
    count(state) {
        return state.count;
    }
}

const mutations = {
    getAllCourse(state, data) {
        state.courseList = data;
    }
}

const actions = {
    async getAllCourse({ commit, state }) {
        try {
            const resp = await axios.get(config.baseUrl + '/course/')
            commit("getAllCourse", resp.data.data);
        } catch (e) {
            console.log(e);
            commit('getAllCourse', [])
        }

    },
    async getCourseDetail({ commit, state }, courseId) {
        try {
            const resp = await axios.get(config.baseUrl + `/course/${courseId}/`);
            return resp.data.data;
        } catch (e) {
            console.log(e);
            return {};
        }
    },
    async getChapters({ commit, state }, courseId) {
        try {
            const resp = await axios.get(config.baseUrl + `/course/${courseId}/`);
            return resp.data.data;
        } catch (e) {
            console.log(e);
            return [];
        }
    }
}


export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
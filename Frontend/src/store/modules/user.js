import types from '../types.js'

const state = {
    phoneArea: [
        { label: "中国(+86)", value: 0 },
        { label: "中国香港(+852)", value: 1 },
        { label: "中国澳门(+853)", value: 2 },
        { label: "中国台湾(+886)", value: 3 },
        { label: "美国(+1)", value: 4 },
        { label: "加拿大(+1)", value: 5 },
        { label: "马来西亚(+60)", value: 6 },
        { label: "澳洲(+61)", value: 7 },
        { label: "日本(+81)", value: 8 },
        { label: "韩国(+82)", value: 9 },
        { label: "新加坡(+65)", value: 10 },
        { label: "英国(+44)", value: 11 },
        { label: "法国(+33)", value: 12 },
        { label: "俄罗斯(+7)", value: 13 },
        { label: "印度(+91)", value: 14 },
        { label: "泰国(+66)", value: 15 },
        { label: "德国(+49)", value: 16 },
    ],
    newsList: [{
            id: 1,
            title: "什么玩意变更啊",
            website: "yitiantian.com",
            publishDevice: "来自安卓",
            type: '42区',
            describe: "具体啥玩意............",
            picture: '/static/news.jpg',
            favorNum: 21,
            commentNum: 10,
            isCollect: false,
            isFavor: true,
            publishTime: '1天14小时前',
            publisher: 'IT精英',
            publishLogo: '/static/publisher.jpg',
            commentList: [{
                id: 1,
                userId: 1,
                username: 'jackin',
                userLogo: '/static/user.jpg',
                commentText: 'you are de shadiao',
                time: '38分钟前发布',
                device: '来自iPhone',
                stepOnNum: 11,
                diggNum: 0,
                child: [{
                        id: 2,
                        userId: 2,
                        username: 'alex',
                        userLogo: '/static/user.jpg',
                        commentText: 'are you shadiao',
                        time: '38分钟前发布',
                        device: '来自iPhone',
                        stepOnNum: 11,
                        diggNum: 0,
                        child: []
                    },
                    {
                        id: 3,
                        userId: 3,
                        username: 'eric',
                        userLogo: '/static/user.jpg',
                        commentText: 'yes you are shadiao',
                        time: '38分钟前发布',
                        device: '来自iPhone',
                        stepOnNum: 11,
                        diggNum: 0,
                        child: []
                    }
                ]
            }, {
                id: 4,
                userId: 4,
                username: 'seven',
                userLogo: '/static/user.jpg',
                commentText: 'yeah are de shadiao',
                time: '38分钟前发布',
                device: '来自iPhone',
                stepOnNum: 11,
                diggNum: 0,
                child: []
            }]
        },
        {
            id: 2,
            title: "什么玩意变更啊",
            website: "yitiantian.com",
            publishDevice: "来自安卓",
            type: '42区',
            describe: "具体啥玩意............",
            picture: '/static/news.jpg',
            favorNum: 21,
            commentNum: 10,
            isCollect: false,
            isFavor: true,
            publishTime: '1天14小时前',
            publisher: 'IT精英',
            publishLogo: '/static/publisher.jpg',
            commentList: []
        },
        {
            id: 3,
            title: "什么玩意变更啊",
            website: "yitiantian.com",
            publishDevice: "来自安卓",
            type: '42区',
            describe: "具体啥玩意............",
            picture: '/static/news.jpg',
            favorNum: 21,
            commentNum: 10,
            isCollect: false,
            isFavor: true,
            publishTime: '1天14小时前',
            publisher: 'IT精英',
            publishLogo: '/static/publisher.jpg',
            commentList: []
        },
        {
            id: 4,
            title: "什么玩意变更啊",
            website: "yitiantian.com",
            publishDevice: "来自安卓",
            type: '42区',
            describe: "具体啥玩意............",
            picture: '/static/news.jpg',
            favorNum: 21,
            commentNum: 10,
            isCollect: false,
            isFavor: true,
            publishTime: '1天14小时前',
            publisher: 'IT精英',
            publishLogo: '/static/publisher.jpg',
            commentList: []
        },
        {
            id: 5,
            title: "什么玩意变更啊",
            website: "yitiantian.com",
            publishDevice: "来自安卓",
            type: '42区',
            describe: "具体啥玩意............",
            picture: '/static/news.jpg',
            favorNum: 21,
            commentNum: 10,
            isCollect: false,
            isFavor: true,
            publishTime: '1天14小时前',
            publisher: 'IT精英',
            publishLogo: '/static/publisher.jpg',
            commentList: []
        },
        {
            id: 6,
            title: "什么玩意变更啊",
            website: "yitiantian.com",
            publishDevice: "来自安卓",
            type: '42区',
            describe: "具体啥玩意............",
            picture: '/static/news.jpg',
            favorNum: 21,
            commentNum: 10,
            isCollect: false,
            isFavor: true,
            publishTime: '1天14小时前',
            publisher: 'IT精英',
            publishLogo: '/static/publisher.jpg',
            commentList: []
        },
        {
            id: 7,
            title: "什么玩意变更啊",
            website: "yitiantian.com",
            publishDevice: "来自安卓",
            type: '42区',
            describe: "具体啥玩意............",
            picture: '/static/news.jpg',
            favorNum: 21,
            commentNum: 10,
            isCollect: false,
            isFavor: true,
            publishTime: '1天14小时前',
            publisher: 'IT精英',
            publishLogo: '/static/publisher.jpg',
            commentList: []
        }, {
            id: 8,
            title: "什么玩意变更啊",
            website: "yitiantian.com",
            publishDevice: "来自安卓",
            type: '42区',
            describe: "具体啥玩意............",
            picture: '/static/news.jpg',
            favorNum: 21,
            commentNum: 10,
            isCollect: false,
            isFavor: true,
            publishTime: '1天14小时前',
            publisher: 'IT精英',
            publishLogo: '/static/publisher.jpg',
            commentList: []
        }
    ]
}

var getters = {
    phoneArea(state) {
        return state.phoneArea;
    },
    newList(state) {
        return state.newList;
    }
}

const actions = {
    increment({ commit, state }) {
        commit(types.INCREMENT);
    }
}

const mutations = {
    [types.INCREMENT](state) {
        state.count++;
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
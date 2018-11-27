var config = {
    prefix: "/django-api",
    apiPrefix: "/api/v1",
    courseFilterList: [{
            name: "all",
            label: "全部"
        },
        {
            name: "first",
            label: "Python"
        },
        {
            name: "second",
            label: "Linux基础"
        },
        {
            name: "third",
            label: "前端"
        },
        {
            name: "four",
            label: "Python进阶"
        },
        {
            name: "five",
            label: "UI"
        },
        {
            name: "six",
            label: "工具"
        },
    ]
}

config.baseUrl = config.prefix + config.apiPrefix;

export default config;
<template>
  <div>
    <div class="brief-area">
      <span class="brief-title">课程概述</span>
      <div>{{courseDetail.brief}}</div>
      <img src="@/assets/python.png" alt="">
    </div>
    <div class="price-area">
      <el-row>
        <el-col v-for="(val, index) in pricePolicy" :key="index" :span="3" :offset="2">
          <div style="height:110px;width:220px;border: 1px solid #eee;text-align:center">
            <div style="margin-top:15px;">￥ {{val.price}}</div>
            <div style="margin-top:10px;">有效期{{val.time}}个月</div>
          </div>
        </el-col>
      </el-row>
      <div class="buy-buttons">
        <el-button type="primary" size="medium">购买</el-button>
        <el-button type="success" size="medium" style="margin-left:30px;">加入购物车</el-button>
      </div>
    </div>
    <div class="why-study">
      <div class="title">为什么学习这门课程</div>
      <div class="content">{{courseDetail.whyStudy}}</div>
      <div class="vip-service">
        <div v-for="(o, v) in 3" :key="v" style="display:inline-block;margin-top:30px;width:20%;text-align:center;margin:20px;">
          <img src="@/assets/vip.png" alt="">
          <div>精彩内容</div>
          <div style="word-wrap:break-word;margin-top:15px;">知名网红讲师根据企业真实需求精心打造的课程内容</div>
        </div>
      </div>
    </div>
    <div class="what-to-study">
      <div class="title">我将学到哪些内容？</div>
      <div class="sub-title">为了帮你掌握金融量化分析入门，你将深入学习如下内容</div>
      <div class="content">
        <el-col v-for="(o, k) in 5" :key="k" :span="6" :offset="2" style="margin-top:30px;text-align:left;">
          <el-card>
            <div>PROJECT 3</div>
            <div>量化投资初试</div>
            <div>量化策略介绍</div>
            <div> 选股、择时、仓位管理、止盈止损、等……</div>
            <div>在线量化投资平台展示及简介</div>
            <div> 获取数据</div>
          </el-card>
        </el-col>
      </div>
      <div style="clear: both;"></div>
    </div>
    <div class="course-requirement">
      <div style="width:60%;text-align:center;margin-left:20%;">
        <div class="requirement-title">此项目如何有助于我的职业生涯？</div>
        <div class="requirement-content">{{courseDetail.career_improvement}}</div>
      </div>
      <div>
        <div style="display:inline-block;width:40%;padding-left:10%;">
          <div class="requirement-title">课程先修要求</div>
          <div class="requirement-content">{{courseDetail.prerequisite}}</div>
        </div>
        <div style="display:inline-block;width:40%;vertical-align: top;padding-left:5%;">
          <div class="requirement-title">推荐课程</div>
          <div class="requirement-content">若你缺乏相关经验，建议学习以下课程</div>
          <div>
            <ul>
              <li v-for="(reCourse, index) in courseDetail.recommend_courses" :key="index" style="margin:5px;">
                <el-button type="success" size="mini" @click="redirectCourse(reCourse.id)">{{reCourse.name}}</el-button>
              </li>
            </ul>
          </div>
        </div>
      </div>

    </div>
    <div class="teachers">
      <div class="title">课程讲师简介</div>
      <div style="padding-left: 20%">
        <el-row>
          <el-col v-for="(teacher, index) in courseDetail.teachers" :key="index" :span="8" :offset="4">
            <el-card :body-style="{ 'text-align':'center' }">
              <img src="@/assets/teacher.png" alt="">
              <div>{{teacher.name}}</div>
              <div>{{teacher.title}}</div>
              <div>{{teacher.brief}}</div>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
  import PlayPng from "@/assets/play.png"

  export default {
    name: "course-item-overview",
    data() {
      return {
        courseDetail: {
          brief: "信息时代，数据为王，互联网包含了迄今为止最有用的数据集，并且大部分可以免费公开访问，但是由于数据被嵌入在众多网站的结构和样式中导致难以被复用，应运而生出现了网络爬虫，使用程序自动获取互联网上的资源。本系列课程将带你开发自动化程序实现数据自动采集，针对众多网站防止数据被获取采取防爬虫方案，课程中包含对防爬策略所有解决方法，专治各种爬虫疑难杂症，同时课程还从源码级别深度剖析流行的爬虫框架，研究如何提高爬虫性能，使你在爬虫方向真正做到“遇鬼杀鬼，遇神杀神，所向披靡”。",
          whyStudy: "成为即懂技术又懂金融的复合型人才，金融和互联网算是当下最有前景的几大行业之一，越来越多的金融公司开始大量使用机器人自动交易，通过量化程序自动选股、买卖等。 对于金融从业者，本课程可以使你把自己数年的投资经验通过程序转化成量化策略模型，然后通过计算机更容易和快速的筛选出符合你投资策略的股票。 对于只懂技术不懂金融的同学，本课程将第一次真正带你进入金融行业，学习股票、期货、量化分析等基础金融知识，掌握各种量化策略原理且能通过程序来实现，还可以开发出自己的策略模型，说不定这会是你成为未来金融大鳄的第一步。",
          career_improvement: "对于不懂金融的程序员，这将是你成为复合型人才的第一步！对于不懂技术的金融从业者，可通过量化分析&交易最大化你的投资收益！",
          prerequisite: "学习此课程前，请确保你已熟练掌握Python基础语法、数据库基础操作、 算法基础知识",
          recommend_courses: [{
            id: 1,
            name: "21天python基础"
          }, {
            id: 2,
            name: "Mysql数据库从入门至进阶"
          }, {
            id: 3,
            name: "算法入门"
          }],
          teachers: [{
              name: "Alex 金角大王",
              title: "路飞学城 金牌讲师",
              brief: "CrazyEye,MadKing,TriAquae三款开源软件作者，10多年运维+自动化开发经验，曾任职公安部、飞信、Nokia中国、汽车之家等公司，热爱技术、电影、音乐、旅游、妹子！",
              img: ""
            },
            {
              name: "Alex 金角大王",
              title: "路飞学城 金牌讲师",
              brief: "CrazyEye,MadKing,TriAquae三款开源软件作者，10多年运维+自动化开发经验，曾任职公安部、飞信、Nokia中国、汽车之家等公司，热爱技术、电影、音乐、旅游、妹子！",
              img: ""
            }
          ]
        },
        pricePolicy: [{
          price: "99",
          time: 1
        }, {
          price: "199",
          time: 2
        }, {
          price: "299",
          time: 3
        }, {
          price: "399",
          time: 6
        }]
      }
    },
    methods: {
      redirectCourse(courseId) {
        this.$router.push({
          name: 'course-detail',
          params: {
            id: courseId
          }
        });
        console.log("跳转");
      }
    }
  }

</script>

<style scoped>
  .brief-area div {
    width: 50%;
    display: inline-block;
    margin-left: 10%;
  }

  .brief-area img {
    display: inline-block;
    width: 20%;
    margin-left: 10%;
    height: 120px;
    vertical-align: bottom;
  }

  .brief-title {
    margin-top: 20px;
    margin-left: 10%;
    font-size: 42px;
    font-weight: bold;
    display: block;
  }

  .price-area {
    margin: 5%;
    font-size: 24px;
    font-weight: bold;
  }

  .buy-buttons {
    width: 100%;
    text-align: center;
    margin-top: 30px;
  }

  .why-study {
    margin-top: 50px;
    width: 100%;
    text-align: center;
  }

  .title {
    font-size: 42px;
    font-weight: bold;
  }

  .why-study .content {
    margin-top: 30px;
    font-size: 24px;
    padding-left: 10%;
    padding-right: 10%;
  }

  .what-to-study {
    margin-top: 50px;
    width: 100%;
    text-align: center;
  }

  .what-to-study .sub-title {
    margin-top: 15px;
    font-size: 24px;
  }


  .course-requirement {
    text-align: left;
  }

  .requirement-title {
    margin-top: 30px;
    font-size: 42px;
    font-family: "仿宋";
  }

  .requirement-content {
    margin-top: 20px;
    font-size: 24px;
    word-wrap: break-word;
  }

  .teachers {
    margin-top: 50px;
    text-align: center;
  }

  .teachers div {
    margin: 5px;
  }

</style>

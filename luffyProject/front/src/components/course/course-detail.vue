<template>
<div>
  <div style="position: relative;">
    <div class="video-body"></div>
    <div class="course-name">金融课</div>
    <div class="course-slogan">口号...</div>
    <img :src="PlayPng" alt="" class="course-img" @click="showVideo">
    <div class="course-info">
      <span>难度 : 中级</span>
      <span>时长 : 20小时</span>
      <span>学习人数 : 176人</span>
      <span>评分 : 9.9</span>
    </div>
  </div>
  <CcVideo ref="video"></CcVideo>
</div>

</template>

<script>
  /**
   * 1.视频部分： 课程名称， 课程口号， 课程级别， 课时/时长， 学生人数，评分， 视频
   *    课程名称：course
   *    课程口号：course_slogan
   *    课程级别：course__level
   *    课时/时长: hours
   *    学生人数：先写死
   *    评分：先写死
   *    
   * 2.tab菜单部分
   *    1）课程概述
   *        模块描述  course__brief
   *        价格策略：1/2/3/6月 价格  course__price_policy
   *        购买，加入购物车
   * 
   *        为什么要学 why_study 
   *        我们将学到什么？ 章节表，课时表  what_to_study_brief
   *        此项目有助于 课程先修和推荐课 career_improvement prerequisite， recommend_courses
   *        老师介绍 teachers
   *    2）课程章节
   * 
   *    3）用户评价
   * 
   *    4）常见问题
   */

  import CcVideo from "@/components/course/cc-video.vue"
  import PlayPng from "@/assets/play.png"

  export default {
    name: "course-detail",
    components: {
      CcVideo
    },
    data() {
      return {
        PlayPng,
        courseDetail: {
          course: "",
          slogon: "",
          why: "",
          recommend_courses: [],
        }
      };
    },
    async created() {
      this.courseDetail = await this.$store.dispatch(
        "course/getCourseDetail",
        this.$route.params.id
      );
    },
    methods: {
      showVideo() {
        this.$refs['video'].showDialog();
      }
    }
  };

</script>

<style scoped>
  .course-name {
    color: white;
    font-size: 45px;
    font-weight: bold;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    text-align: center;
    margin-top: 3%;
  }

.course-slogan{
    color: white;
    font-size: 32px;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    text-align: center;
    margin-top: 8%;
}

.course-img{
    position: absolute;
    left: 0;
    top: 0;
    display: block;
    height: 65px;
    width: 65px;
    margin-top: 12%;
    margin-left: 47%;
    cursor: pointer;
}

.course-info{
    color: white;
    font-size: 24px;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
        text-align: center;
    margin-top: 28%;
}

.course-info span {
  margin: 50px;
}
  .video-body {
    width: 100%;
    height: 500px;
    background-image: url('./../../assets/python.png');
    background-size: 100% 100%;
  }

</style>

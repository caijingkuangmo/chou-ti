<template>
  <div class="course-item" style="margin-top:20px;cursor: pointer;" @click="viewCourseDetail(course.id)">
    <el-card :body-style="{ padding: '0px' }">
      <div style="position:relative">
        <img :src="`${config.prefix}${course.course_img}`" class="image">
        <div class="course-title">{{course.name}}</div>
      </div>
      <div style="padding: 20px;">
        <span class="brief">简介:{{course.brief}}</span>
        <div class="bottom clearfix" style="margin-top:20px;">
          <div style="width:50%;display: inline-block;text-align:left;float:left">123人<span style="margin-left:20px">{{course.level}}</span></div>
          <div style="width:50%;display: inline-block;text-align:right;right:right">免费</div>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
  /**
   * name:标题
   * course_img：背景图
   * brief：课程描述
   * level: 级别
   * 人数：先写死
   * 价格：县写死，这里是一个月价格
   */
  // import pythonImg from "@/assets/python.png"
  import config from "@/config/config.js"

  export default {
    name: "course-item",
    props: {
      course: {
        type: Object,
        default: function () {
          return {
            name: "",
            course_img: "",
            brief: "",
            level: "",
          };
        }
      }
    },
    created() {},
    data() {
      return {
        config,
      }
    },
    methods: {
      viewCourseDetail(course_id) {
        this.$router.push({
          name: 'course-detail',
          params: {
            id: course_id
          }
        });
      }
    }
  }

</script>

<style scoped>
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }

  .clearfix:after {
    clear: both
  }

  .course-title {
    position: absolute;
    height: 100%;
    width: 100%;
    left: 0;
    top: 0;
    text-align: center;
    padding-top: 15%;
    background: rgba(255, 255, 255, .5);
  }

  .brief {
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    display: inline-block;
    width: 90%
  }

</style>

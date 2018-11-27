<template>
  <div class="course-item">
    <el-row>
      <el-col :span="8" v-for="(o, index) in 2" :key="o" :offset="index > 0 ? 2 : 0">
        <!-- <el-card :body-style="{ padding: '0px' }">
          <img :src="pythonImg" class="image">
          <div style="padding: 14px;">
            <span>好吃的汉堡</span>
            <div class="bottom clearfix">
              <time class="time">{{ currentDate }}</time>
              <el-button type="text" class="button">操作按钮</el-button>
            </div>
          </div>
        </el-card> -->
        <el-card :body-style="{ padding: '0px' }">
          <div style="position:relative">
            <img :src="pythonImg" class="image">
            <div class="course-title">Python基础</div>
          </div>
          <div style="padding: 20px;">
            <span class="brief">简介：123sfdaaaaaaaaaaaaaaaaaasdffhdfffffffffffffffffffffffffffffffffffffffffffffffffffffff456</span>
            <div class="bottom clearfix" style="margin-top:20px;">
              <div style="width:50%;display: inline-block;text-align:center;float:left">123人</div>
              <div style="width:50%;display: inline-block;text-align:center;right:right">免费</div>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
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
  import pythonImg from "@/assets/python.png"

  export default {
    name: "course-item",
    props: {
      course: {
        type: Object,
        default: function () {
          return {};
        }
      }
    },
    created() {
      console.log(this.course);
    },
    data() {
      return {
        pythonImg,
      }
    }
  }

</script>

<style scoped>
  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
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

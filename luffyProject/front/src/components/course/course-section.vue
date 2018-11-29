<template>
  <div style="font-size:24px;">
    <el-row class="section-item" v-for="(section, index) in sectionList" :key="index">
      <div @click="showCcVideo(section.sectionLink)">
        <el-col :span="12" style="text-align:left" :offset="6">
          <span>{{section.name}}</span>
          <span v-if="section.freeTrail" style="margin-left:30px">
            <el-button>免费试看</el-button>
          </span>
        </el-col>
        <el-col :span="6">
          <img src="@/assets/play.png" style="width:35px; height:35px">
          <span style="margin-left: 15px;vertical-align: top;">{{section.videoTime}}</span>
        </el-col>
      </div>
    </el-row>

    <CcVideo ref="video"></CcVideo>
  </div>
</template>

<script>
  import CcVideo from "@/components/course/cc-video.vue"
  export default {
    name: "course-section",
    props: {
      chapterId: {
        type: Number,
      }
    },
    created() {
      //请求课时 目录
      console.log(this.chapterId);
    },
    components: {
      CcVideo
    },
    data() {
      return {
        sectionList: [{
            name: "影响股价因素&股票买卖知识",
            videoTime: "17:45",
            sectionLink: "",
            freeTrail: true
          },
          {
            name: "影响股价因素&股票买卖知识",
            videoTime: "17:45",
            sectionLink: "",
            freeTrail: false
          },
          {
            name: "影响股价因素&股票买卖知识",
            videoTime: "17:45",
            sectionLink: "",
            freeTrail: false
          },
        ]
      }
    },
    methods: {
      showCcVideo(ccid) {
        console.log('ccid', ccid);
        //需要对是否免费和登陆做验证
        this.$refs['video'].showDialog();
      }
    }
  }

</script>

<style scoped>
  .section-item {
    margin-top: 15px;
    margin-bottom: 15px;

  }
.el-row:hover {
    background: #eee;
    cursor: pointer;
}
</style>

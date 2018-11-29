<template>
  <div>
    <div v-for="(cha, index) in chapterList" :key="index">
      <el-row class="chapter-item">
        <el-col :span="2" style="text-align:center" :offset="4">
          <i class="el-icon-document"></i>
        </el-col>
        <el-col :span="16">
            第{{cha.chapter}}章-{{cha.name}}
        </el-col>
      </el-row>
    <CourseSection :chapterId="cha.id"></CourseSection>
    </div>

  </div>
</template>

<script>
import CourseSection from "@/components/course/course-section.vue"
  export default {
    name: "course-item-chapter",
    components: {
        CourseSection,
    },
    created() {
      //请求章节信息
      //需要一个course id
    },
    data() {
      return {
        chapterList: [{
            id: 1,
            chapter: 1,
            name: "金融、股票知识入门"
          },
          {
            id: 2,
            chapter: 2,
            name: "科学计算基础包——numpy"
          },
          {
            id: 3,
            chapter: 3,
            name: "数据分析核心包——pandas"
          }
        ]
      }
    }
  }

</script>

<style scoped>
  .chapter-item {
    margin-top: 50px;
    font-size: 42px;
  }

</style>

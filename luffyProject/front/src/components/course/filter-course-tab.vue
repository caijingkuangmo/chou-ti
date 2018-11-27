<template>
  <div class="filter-course-area">
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane v-for="(item, index) in config.courseFilterList" :key="index" :label="item.label" :name="item.name">
        <div>
          <CourseItem v-for="(course, index) in courseList" :key="index" :course="course"></CourseItem>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
  import config from "@/config/config.js";
  import CourseItem from "@/components/course/course-item.vue";
  export default {
    name: "filter-course-tab",
    props: [],
    data() {
      return {
        activeName: "all",
        courseList: [{name:'123'}],
        config,
      }
    },
    components:{
      CourseItem,
    },
    created() {
      //请求后端所有课程
    },
    methods: {
      handleClick(tab, event) {
        this.activeName = tab.name;
        //请求vuex 进行筛选
        console.log('filter-course', tab.name, tab.label);
      }
    }
  }

</script>

<style scoped>

</style>

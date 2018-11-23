<template>
    <div>
        <div>课程名称:{{ courseDetail.course }}</div>
        <div>课程口号:{{ courseDetail.slogon }}</div>
        <div>为什么学:{{ courseDetail.why }}</div>

        推荐课程:
        <div v-for="(c,index) in courseDetail.recommend_courses" :key="index">
            <div>{{ c }}</div>
        </div>
    </div>
</template>

<script>
export default {
  name: "course-detail",
  data() {
    return {
      courseDetail: {
          course:"",
          slogon:"",
          why:"",
          recommend_courses:[],
      }
    };
  },
  async created() {
    this.courseDetail = await this.$store.dispatch(
      "course/getCourseDetail",
      this.$route.params.id
    );
  }
};
</script>

<style scoped>
</style>



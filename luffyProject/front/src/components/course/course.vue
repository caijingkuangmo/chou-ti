<template>
  <div>
    <Nav></Nav>
    <CourseFilterTab></CourseFilterTab>
  </div>
</template>

<script>
  import CourseFilterTab from "@/components/course/filter-course-tab.vue"

  import Nav from "@/components/index.vue";
  export default {
    name: "course",
    components: {
      Nav,
      CourseFilterTab,
    },
    async created() {
      await this.$store.dispatch("course/getAllCourse");
    },
    data() {
      return {
      };
    },
    computed: {
      courseList() {
        return this.$store.state.course.courseList;
      },
    },
    methods: {
      viewCourseDetail(row) {
        this.$router.push({
          name: 'course-detail',
          params: {
            id: row.id
          }
        });
      }
    }
  };

</script>

<style scoped>
</style>

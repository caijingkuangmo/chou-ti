<template>
    <div>
        <Nav></Nav>
        <div class="course-display-area">
            <el-table :data="courseList" style="width: 100%">
                <el-table-column prop="id" label="ID" width="180">
                </el-table-column>
                <el-table-column prop="level" label="级别" width="180">
                </el-table-column>
                <el-table-column prop="name" label="名称" width="180">
                </el-table-column>
                <el-table-column prop="course_img" label="图片链接" width="180">
                </el-table-column>
                <el-table-column label="操作" width="180">
                    <template slot-scope="scope">
                        <el-button @click="viewCourseDetail(scope.row)" type="text">查看课程详细</el-button>
                        <!-- <router-link :to="{name:'course-detail', params:{id:scope.row.id}}">查看课程详细</router-link> -->
                    </template>
                </el-table-column>
            </el-table>
        </div>
    </div>
</template>

<script>
import Nav from "@/components/index.vue";
export default {
  name: "course",
  components: {
    Nav
  },
  async created() {
    await this.$store.dispatch("course/getAllCourse");
  },
  data() {
    return {};
  },
  computed: {
    courseList() {
      return this.$store.state.course.courseList;
    }
  },
  methods: {
    viewCourseDetail(row) {
      this.$router.push({name:'course-detail', params:{id:row.id}});
    }
  }
};
</script>

<style scoped>
</style>


